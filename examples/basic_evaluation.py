"""
A minimal working example that demonstrates how to use a custom adapter
with the AgentUnit framework.
"""

from agentunit.adapters.base import BaseAdapter
from agentunit.core.schema import DatasetCase, TraceLog, AdapterOutcome


class FakeAdapter(BaseAdapter):
    """
    A simple mock adapter used only for demonstration.
    It returns a predictable output so evaluation is easy to understand.
    """

    def prepare(self):
        # No preparation needed
        pass

    def execute(self, case: DatasetCase, trace: TraceLog) -> AdapterOutcome:
        # Create predictable output
        output = f"Fake response to: {case.prompt}"
        return AdapterOutcome(output=output)


def main():
    # Step 1 — Create a FakeAdapter
    adapter = FakeAdapter()

    # Step 2 — Prepare the dataset case
    case = DatasetCase(prompt="Say hello!")

    # Step 3 — Prepare a trace log
    trace = TraceLog()

    # Step 4 — Execute using the adapter
    result = adapter.execute(case, trace)

    # Step 5 — Print results
    print("Prompt:", case.prompt)
    print("Model Output:", result.output)


if __name__ == "__main__":
    main()
