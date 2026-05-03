from typing import List
from ..models.task import ExecutionPlan, CodeChange

class CodeTransformer:
    """Simulates AST-safe code modifications across the file system."""
    
    def transform(self, plan: ExecutionPlan) -> List[CodeChange]:
        print(f"[CodeTransformer] Executing {len(plan.steps)} steps...")
        changes = []
        
        for step in plan.steps:
            print(f"  -> Applying change: {step.action} on {step.target}")
            
            # Simulate the diff that would be generated
            diff = f"--- a/{step.target}\n+++ b/{step.target}\n@@ -0,0 +1,10 @@\n+# {step.detail}\n"
            
            changes.append(CodeChange(
                file_path=step.target,
                change_type=step.action,
                diff=diff
            ))
            
        return changes
