# Agentic Data Analyst

A deterministic, tool-using agent foundation for safe data-analysis workflows. The project demonstrates routing, tool allow-lists, structured results, and a reviewable execution trace without hiding side effects behind a black box.

## Features

- Explicit tool registry and allow-list.
- Deterministic routing for profiling, statistics, and help requests.
- Structured JSON-serializable responses.
- No shell execution and no network access from tools.
- Unit tests for routing, safety, and failure handling.

## Run

```bash
python -m agentic_data_analyst.cli --question "profile the dataset" --data examples/sample.csv
```

This is a portfolio foundation, not a production autonomous agent. Production extensions should add authentication, tracing, rate limits, human approval for consequential actions, and model-backed planning behind the same tool contracts.
