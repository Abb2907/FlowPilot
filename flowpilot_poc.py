import json
import os
from typing import Dict, List, Any
import datetime

class FlowPilotEngine:
    """Core engine for FlowPilot proof-of-concept."""

    def __init__(self, developer_mode="expert"):
        self.developer_mode = developer_mode
        self.context = {}

    def handle_input(self, text_input: str) -> Dict[str, Any]:
        """Accepts natural language or structured ticket."""
        print(f"[*] Processing Input: '{text_input}'")
        return {
            "task_id": "FP-" + datetime.datetime.now().strftime("%Y%m%d%H%M"),
            "intent": "feature_addition",
            "description": text_input
        }

    def decompose_task(self, task: Dict[str, Any]) -> List[Dict[str, str]]:
        """Analyzes intent and generates execution plan."""
        print("[*] Decomposing task into steps...")
        if "authentication" in task['description'].lower():
            return [
                {"step": 1, "action": "add_dependency", "target": "requirements.txt", "detail": "Add pyjwt"},
                {"step": 2, "action": "create_file", "target": "auth.py", "detail": "Implement JWT logic"},
                {"step": 3, "action": "modify_file", "target": "main.py", "detail": "Add auth middleware"}
            ]
        return [{"step": 1, "action": "unknown", "detail": "Generic fallback step"}]

    def transform_code(self, plan: List[Dict[str, str]]):
        """Simulates file modification across the repo."""
        for step in plan:
            print(f"  -> Executing Step {step['step']}: {step['action']} on {step['target']}")
            # In a real tool, AST parsing and file writes happen here

    def generate_tests(self, task: Dict[str, Any]):
        """Creates unit/integration tests."""
        print(f"[*] Generating test suite for {task['task_id']}...")
        print("  -> Created test_auth.py with 4 unit tests (Edge cases covered).")

    def explain_changes(self, plan: List[Dict[str, str]]):
        """Explanation Layer tailored to Developer Mode."""
        print(f"\n[*] Explaining Changes ({self.developer_mode.upper()} MODE):")
        for step in plan:
            if self.developer_mode == "beginner":
                print(f"  - We updated {step['target']} to {step['detail'].lower()}. This is necessary so the app can securely verify users without storing session data.")
            else:
                print(f"  - Mod: {step['target']} | Reason: {step['detail']}")

    def generate_pr_automation(self, task: Dict[str, Any], plan: List[Dict[str, str]]):
        """Generates PR metadata."""
        print("\n[*] PR Automation:")
        print(f"  Title: Feat: {task['description']}")
        print(f"  Summary: Automated implementation of {task['description']}. Modified {len(plan)} files.")

    def run(self, input_text: str):
        task = self.handle_input(input_text)
        plan = self.decompose_task(task)
        self.transform_code(plan)
        self.generate_tests(task)
        self.explain_changes(plan)
        self.generate_pr_automation(task, plan)

if __name__ == "__main__":
    pilot = FlowPilotEngine(developer_mode="beginner")
    print("--- FlowPilot Workflow Demonstration ---")
    pilot.run("Add user authentication with JWT")
