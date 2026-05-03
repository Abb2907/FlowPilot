from .core.input_handler import InputHandler
from .core.task_decomposer import TaskDecomposer
from .core.code_transformer import CodeTransformer
from .core.explainer import Explainer
from .core.test_generator import TestGenerator
from .core.pr_automation import PRAutomation
from .models.task import Task

class FlowPilotCLI:
    """The main CLI entry point for FlowPilot."""
    
    def __init__(self, developer_mode="expert"):
        self.input_handler = InputHandler()
        self.decomposer = TaskDecomposer()
        self.transformer = CodeTransformer()
        self.explainer = Explainer(mode=developer_mode)
        self.test_generator = TestGenerator()
        self.pr_automation = PRAutomation()

    def run(self, input_text: str):
        print("="*50)
        print("[*] FlowPilot Initializing...")
        print("="*50)
        
        # 1. Handle Input
        request = self.input_handler.process_input(input_text)
        
        # 2. Decompose Task
        plan = self.decomposer.decompose(request)
        
        # 3. Transform Code
        changes = self.transformer.transform(plan)
        
        # 4. Generate Tests
        self.test_generator.generate(request, plan)
        
        # 5. Explain Changes
        self.explainer.generate_explanations(plan)
        
        # 6. Automate PR
        self.pr_automation.generate_artifacts(request, changes)
        
        print("\n[*] Task completed successfully!")
        print("="*50)

if __name__ == "__main__":
    import sys
    mode = "expert"
    if len(sys.argv) > 1 and sys.argv[1] == "--beginner":
        mode = "beginner"
        
    cli = FlowPilotCLI(developer_mode=mode)
    cli.run("Add user authentication with JWT")
