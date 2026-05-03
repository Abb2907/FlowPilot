from typing import List
from ..models.task import ExecutionPlan

class Explainer:
    """Generates human-readable explanations based on Developer Mode."""
    
    def __init__(self, mode: str = "expert"):
        self.mode = mode.lower()
        
    def generate_explanations(self, plan: ExecutionPlan) -> List[str]:
        print(f"\n[Explainer] Generating explanations ({self.mode.upper()} MODE):")
        explanations = []
        
        for step in plan.steps:
            if self.mode == "beginner":
                explanation = f"We updated `{step.target}`. This is necessary because: {step.detail.lower()}."
                print(f"  - {explanation}")
            else:
                explanation = f"Mod: {step.target} | Reason: {step.detail}"
                print(f"  - {explanation}")
                
            explanations.append(explanation)
            
        return explanations
