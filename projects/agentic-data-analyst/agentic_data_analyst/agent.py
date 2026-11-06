from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class AgentResult:
    intent: str
    answer: dict
    trace: tuple[str, ...]


def _profile_csv(path: str) -> dict:
    p = Path(path)
    if p.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are accepted by the safe profile tool")
    with p.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {"rows": len(rows), "columns": list(rows[0].keys()) if rows else [], "missing_values": {k: sum(not r.get(k) for r in rows) for k in (rows[0].keys() if rows else [])}}


class SafeAgent:
    def __init__(self) -> None:
        self.tools: dict[str, Callable[..., dict]] = {"profile_csv": _profile_csv}

    def run(self, question: str, *, data: str | None = None) -> AgentResult:
        q = question.lower()
        if "profile" in q or "describe" in q:
            if not data:
                raise ValueError("A CSV path is required for profiling")
            answer = self.tools["profile_csv"](data)
            return AgentResult("profile", answer, ("route:profile", "tool:profile_csv", "review:static"))
        if "help" in q:
            return AgentResult("help", {"supported_intents": ["profile"]}, ("route:help",))
        return AgentResult("unknown", {"message": "Supported request: profile a CSV dataset"}, ("route:unknown",))
