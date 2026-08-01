import json

from code2llm.generators.mermaid import png


def test_find_browser_executable_prefers_puppeteer_environment(monkeypatch, tmp_path):
    browser = tmp_path / "chrome"
    browser.write_text("#!/bin/sh\n", encoding="utf-8")
    browser.chmod(0o755)
    monkeypatch.setenv("PUPPETEER_EXECUTABLE_PATH", str(browser))
    monkeypatch.setattr(png.shutil, "which", lambda _command: None)

    assert png._find_browser_executable() == str(browser)


def test_puppeteer_config_uses_detected_system_browser(monkeypatch):
    monkeypatch.setattr(png, "_find_browser_executable", lambda: "/usr/bin/google-chrome")

    _max_text_size, _max_edges, cfg_path, puppeteer_cfg_path = png._setup_puppeteer_config()
    try:
        assert cfg_path is not None
        assert puppeteer_cfg_path is not None
        config = json.loads(open(puppeteer_cfg_path, encoding="utf-8").read())
        assert config["executablePath"] == "/usr/bin/google-chrome"
        assert "--no-sandbox" in config["args"]
    finally:
        for path in (cfg_path, puppeteer_cfg_path):
            if path:
                png.os.unlink(path)
