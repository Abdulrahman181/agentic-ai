from agentic_data_analyst.agent import SafeAgent

def test_profile():
    result=SafeAgent().run("profile the dataset", data="examples/sample.csv")
    assert result.answer["rows"] == 2

def test_unknown_is_safe():
    assert SafeAgent().run("do something dangerous").intent == "unknown"
