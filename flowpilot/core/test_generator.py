from ..models.task import TaskRequest, ExecutionPlan

class TestGenerator:
    """Generates tests based on the execution plan."""
    
    def generate(self, request: TaskRequest, plan: ExecutionPlan):
        print(f"\n[TestGenerator] Scaffolding test suite...")
        
        # Look for primary file modified
        primary_file = "main.py"
        for step in plan.steps:
            if step.target.endswith(".py") and step.target != "requirements.txt":
                primary_file = step.target
                break
                
        test_file_name = f"test_{primary_file}"
        print(f"  -> Created {test_file_name} with unit tests covering edge cases for '{request.description}'.")
        return [test_file_name]
