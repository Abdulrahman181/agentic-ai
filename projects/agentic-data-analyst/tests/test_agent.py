from pathlib import Path

from agentic_data_analyst.agent import SafeAgent


SAMPLE = Path(__file__).parents[1] / "examples" / "sample.csv"


def test_profile():
    result = SafeAgent().run("profile the dataset", data=str(SAMPLE))
    assert result.answer["rows"] == 2


def test_unknown_is_safe():
    assert SafeAgent().run("do something dangerous").intent == "unknown"
