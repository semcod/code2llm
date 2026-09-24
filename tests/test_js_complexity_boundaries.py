"""Regressions for real JS/TS functions and their decision boundaries (PLF-029)."""

from collections import defaultdict

import pytest

from code2llm.core.lang.typescript import analyze_typescript_js


def analyze(source, ext=".js"):
    return analyze_typescript_js(source, "fixture" + ext, "fixture", ext, defaultdict(int))


def complexities(result):
    return {f.name: f.complexity["cyclomatic_complexity"] for f in result["functions"].values()}


def test_variables_and_expression_arrows_do_not_borrow_the_next_body():
    result = analyze("""
let pending = null, ready = false;
const imported = require('./other');
const pick = () => true;
function unrelated(flag) { if (flag) { return 1; } return 0; }
""")
    assert complexities(result) == {"pick": 1, "unrelated": 2}
    assert result["functions"]["fixture.pick"].calls == []


def test_decisions_belong_to_their_function_even_on_one_line():
    result = analyze("const first = x => x ? yes() : no(); const second = () => true;")
    assert complexities(result) == {"first": 2, "second": 1}
    assert set(result["functions"]["fixture.first"].calls) == {"fixture.yes", "fixture.no"}
    assert not result["functions"]["fixture.second"].calls


def test_strings_comments_regex_and_nested_callbacks_do_not_inflate_parent():
    result = analyze(r"""
function outer(items) {
  const text = 'if (x) { while (x) { ?? && || ? :';
  const matcher = /if|while|\{\}/;
  // if (forbidden) { for (;;) {} }
  return items.map(x => { if (x && x.ok) return 1; return 0; });
}
""")
    funcs = result["functions"]
    assert funcs["fixture.outer"].complexity["cyclomatic_complexity"] == 1
    callbacks = [f for f in funcs.values() if f.name.startswith("<anonymous@")]
    assert len(callbacks) == 1
    assert callbacks[0].complexity["cyclomatic_complexity"] == 3


def test_real_branch_types_and_template_expressions_are_counted():
    result = analyze("""
function work(xs, user) {
  for (const x of xs) { if (x) continue; }
  while (xs.length) xs.pop();
  do { xs.pop(); } while (xs.length);
  try { load(); } catch (e) { log(e); }
  switch (user.kind) { case 'a': break; case 'b': break; default: break; }
  return `${user?.name ?? (xs.length > 0 ? 'yes' : 'no')}`;
}
""")
    assert complexities(result) == {"work": 11}


def test_multiline_typed_arrows_classes_and_nested_names():
    result = analyze(
        """
import type { Item } from './types';
const identity = <T,>(value: T): T => value;
class Service {
  run = (value: number): number => value > 0 ? value : 0;
  read(value: boolean): number { return value ? 1 : 0; }
}
function outer() { function same(x: boolean) { return x ? 1 : 0; } return same(true); }
function another() { function same() { return 0; } return same(); }
""",
        ".ts",
    )
    funcs = result["functions"]
    assert funcs["fixture.identity"].complexity["cyclomatic_complexity"] == 1
    assert funcs["fixture.Service.run"].complexity["cyclomatic_complexity"] == 2
    assert funcs["fixture.outer.same"].complexity["cyclomatic_complexity"] == 2
    assert funcs["fixture.another.same"].complexity["cyclomatic_complexity"] == 1
    assert set(result["classes"]["fixture.Service"].methods) == {
        "fixture.Service.run",
        "fixture.Service.read",
    }
    assert result["module"].imports == ["./types"]


def test_typescript_and_tsx_use_their_own_grammar_in_the_same_process():
    assert complexities(analyze("const value = <number>42;", ".ts")) == {}
    assert complexities(analyze("const View = () => <div>{ok ? 'yes' : 'no'}</div>;", ".tsx")) == {
        "View": 2
    }
    assert complexities(analyze("const value = <number>42;", ".ts")) == {}


def test_invalid_syntax_is_not_reported_as_a_low_complexity_success():
    with pytest.raises(ValueError, match="invalid JavaScript/TypeScript syntax"):
        analyze("function broken( {")


def test_default_parameter_expressions_and_named_expression_binding():
    result = analyze("const exposed = function inner(x = ready ? yes() : no()) { return x; };")
    assert complexities(result) == {"exposed": 2}
    assert set(result["functions"]["fixture.exposed"].calls) == {"fixture.yes", "fixture.no"}


def test_complex_anonymous_callbacks_remain_visible_to_quality_gates():
    branches = "\n".join(f"if (x === {i}) return {i};" for i in range(25))
    result = analyze("function outer(xs) { return xs.map(x => {" + branches + "}); }")
    values = list(complexities(result).values())
    assert sorted(values) == [1, 26]
