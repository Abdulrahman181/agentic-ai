import argparse, json
from .agent import SafeAgent

def main() -> None:
    p=argparse.ArgumentParser(description="Run the safe deterministic data analyst agent")
    p.add_argument("--question", required=True)
    p.add_argument("--data")
    args=p.parse_args()
    result=SafeAgent().run(args.question, data=args.data)
    print(json.dumps({"intent":result.intent,"answer":result.answer,"trace":result.trace}, indent=2))

if __name__ == "__main__": main()
