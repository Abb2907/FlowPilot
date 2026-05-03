from typing import List
from ..models.task import TaskRequest, ExecutionPlan, ExecutionStep

class TaskDecomposer:
    """Simulates an LLM breaking down a request into specific execution steps."""
    
    def decompose(self, request: TaskRequest) -> ExecutionPlan:
        print(f"[TaskDecomposer] Decomposing task: {request.description[:50]}...")
        
        desc = request.description.lower()
        steps = []
        
        if "auth" in desc or "jwt" in desc:
            steps = [
                ExecutionStep(step_num=1, action="add_dependency", target="requirements.txt", detail="Add pyjwt for stateless sessions"),
                ExecutionStep(step_num=2, action="create_file", target="auth.py", detail="Implement JWT encoding/decoding logic"),
                ExecutionStep(step_num=3, action="modify_file", target="main.py", detail="Inject auth middleware into FastAPI app")
            ]
        elif "db" in desc or "database" in desc:
            steps = [
                ExecutionStep(step_num=1, action="add_dependency", target="requirements.txt", detail="Add sqlalchemy"),
                ExecutionStep(step_num=2, action="create_file", target="database.py", detail="Set up SQLAlchemy engine and session"),
                ExecutionStep(step_num=3, action="create_file", target="models.py", detail="Create SQLAlchemy ORM models")
            ]
        else:
            steps = [
                ExecutionStep(step_num=1, action="modify_file", target="main.py", detail=f"Implement: {request.description}")
            ]
            
        return ExecutionPlan(task_id=request.id, steps=steps)
