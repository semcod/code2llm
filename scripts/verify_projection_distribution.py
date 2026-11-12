"""Qualify the public projection exporter in installed wheel and sdist artifacts.

Run with ``python -I`` to exclude the checkout from import resolution. The
artifact mode creates a separate, empty venv for each distribution; neither
an editable checkout nor a manually copied exporter can satisfy this check.
This verifies the projection contract, not the bytes of its source inputs.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
from importlib import metadata
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import venv


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(value):
    data = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(data.encode("utf-8")).hexdigest()


def check_document(document, expected_version):
    require(document["schema"] == "code2llm.projection/v1", "Unexpected projection schema")
    require(document["producer"] == {"tool": "code2llm", "version": expected_version},
            "Missing or mismatched producer identity")
    records = document["records"]
    require(document["digest"] == digest(records), "Invalid projection digest")
    for record in records:
        content = {key: value for key, value in record.items() if key != "digest"}
        require(record["digest"] == digest(content), "Invalid record digest")


def check_installed(expected_version):
    import code2llm
    from code2llm.exporters import ProjectionsExporter, build_projection, get_exporter
    from code2llm.exporters import projections_exporter

    require(Path(code2llm.__file__).resolve().is_relative_to(Path(sys.prefix).resolve()),
            "Imported checkout instead of the installed distribution")
    distribution = metadata.distribution("code2llm")
    require(code2llm.__version__ == distribution.version == expected_version,
            "Distribution and producer versions differ from the release")
    entry = next((entry for entry in distribution.files or ()
                  if str(entry) == "code2llm/exporters/projections_exporter.py"), None)
    require(entry is not None and entry.hash is not None, "Exporter missing from installed RECORD")
    installed_path = Path(distribution.locate_file(entry)).resolve()
    require(installed_path == Path(projections_exporter.__file__).resolve(),
            "Exporter was loaded outside the distribution")
    actual_hash = base64.urlsafe_b64encode(hashlib.sha256(installed_path.read_bytes()).digest()).rstrip(b"=").decode()
    require(entry.hash.mode == "sha256" and entry.hash.value == actual_hash,
            "Exporter differs from installed RECORD")
    require(get_exporter("projections") is ProjectionsExporter, "Public registry lacks projections")
    require(projections_exporter.MAX_RECORDS == 2048 and projections_exporter.FIELD_LIMIT == 200,
            "Projection v1 bounds differ from the consumer contract")

    long_field = "ą" * (projections_exporter.FIELD_LIMIT + 10)
    functions = [SimpleNamespace(name=f"f{i}", qualified_name=long_field + str(i),
                                file=long_field + ".py", line=i + 1)
                 for i in range(projections_exporter.MAX_RECORDS + 1)]
    fixture = SimpleNamespace(modules=[], classes=[], functions=functions,
                              stats={"files": 1, "lines": len(functions)},
                              project_path="projection-contract", analysis_mode="standard")
    expected = build_projection(fixture)
    check_document(expected, expected_version)
    require(len(expected["records"]) == projections_exporter.MAX_RECORDS
            and expected["stats"]["truncated"] is True, "Record bound was not reported")
    require(all(len(record[key]) <= projections_exporter.FIELD_LIMIT
                for record in expected["records"] for key in ("file", "symbol")),
            "Fields exceed the public bound")
    # Exercise the checker against deliberately invalid evidence as well.
    for invalid in ({**expected, "digest": "sha256:" + "0" * 64},
                    {**expected, "producer": {}}):
        try:
            check_document(invalid, expected_version)
        except RuntimeError:
            pass
        else:
            raise RuntimeError("Invalid projection was accepted")
    with tempfile.TemporaryDirectory(prefix="projection-contract-") as directory:
        first = Path(directory) / "first.json"
        second = Path(directory) / "second.json"
        exporter = ProjectionsExporter()
        require(exporter.export(fixture, str(first)) == first, "Export path differs")
        exporter.export(fixture, str(second))
        require(first.read_bytes() == second.read_bytes(), "Export bytes are nondeterministic")
        observed = json.loads(first.read_text(encoding="utf-8"))
        require(observed == expected, "Public builder and exporter differ")
        check_document(observed, expected_version)
    check_incremental_api()
    return {"status": "PASS", "version": expected_version,
            "projection_digest": expected["digest"], "records": len(expected["records"]),
            "source_bytes_verified": False}


def check_incremental_api():
    """Exercise installed public analysis independently of the source test tree."""
    from copy import deepcopy
    from code2llm.api import FAST_CONFIG, analyze_file, analyze_incremental

    with tempfile.TemporaryDirectory(prefix="incremental-contract-") as directory:
        root = Path(directory)
        project = root / "project"
        project.mkdir()
        source = project / "a.py"
        source.write_text("def first():\n    return 1\n")
        (project / "b.py").write_text("def other():\n    return 2\n")
        config = deepcopy(FAST_CONFIG)
        config.performance.parallel_enabled = False
        cache = str(root / "private-cache")
        first = analyze_incremental(str(project), cache_dir=cache, config=config)
        warm = analyze_incremental(str(project), cache_dir=cache, config=config)
        require(warm.identity == first.identity and warm.incremental["analysis_candidates"] == 0,
                "Unchanged installed analysis did not reuse its verified cache")
        old = source.stat()
        source.write_text("def later():\n    return 1\n")
        os.utime(source, ns=(old.st_atime_ns, old.st_mtime_ns))
        changed = analyze_incremental(str(project), cache_dir=cache, config=config, changed_files=[])
        cold = analyze_incremental(str(project), cache_dir=cache, config=config, cache_policy="off")
        require(set(changed.analysis.functions) == set(cold.analysis.functions) == {"a.later", "b.other"},
                "Metadata-preserving rewrite reused stale installed analysis")
        require(changed.identity == cold.identity and changed.identity["snapshot_atomic"] is False,
                "Installed observation has a false snapshot claim")
        require(set(analyze_file(str(source), config).functions) == {"a.later"},
                "Installed analyze_file scanned a sibling")


def check_artifacts(directory, expected_version):
    directory = directory.resolve()
    wheels = sorted(directory.glob("code2llm-*.whl"))
    sources = sorted(directory.glob("code2llm-*.tar.gz"))
    require(len(wheels) == len(sources) == 1, "Exactly one wheel and one sdist are required")
    installer = shutil.which("uv")
    require(installer is not None, "Install uv to qualify isolated distributions")
    results = []
    script = str(Path(__file__).resolve())
    for artifact in [*wheels, *sources]:
        with tempfile.TemporaryDirectory(prefix="projection-install-") as temporary:
            root = Path(temporary)
            environment = root / "venv"
            venv.EnvBuilder().create(environment)
            python = environment / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
            subprocess.run([installer, "pip", "install", "--python", str(python), str(artifact)],
                           cwd=root, check=True, timeout=300)
            observed = subprocess.run([str(python), "-I", script,
                                       "--expected-version", expected_version],
                                      cwd=root, check=True, capture_output=True, text=True, timeout=60)
            results.append({"artifact": artifact.name,
                            "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
                            "check": json.loads(observed.stdout)})
    require(results[0]["check"]["projection_digest"] == results[1]["check"]["projection_digest"],
            "Wheel and sdist produce different projections")
    return {"status": "PASS", "artifacts": results, "forge_consumer": "NOT_RUN"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-version", required=True)
    parser.add_argument("--artifact-directory", type=Path)
    args = parser.parse_args()
    result = (check_artifacts(args.artifact_directory, args.expected_version)
              if args.artifact_directory else check_installed(args.expected_version))
    print(json.dumps(result, sort_keys=True))
