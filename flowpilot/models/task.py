from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime

class TaskType(str, Enum):
    FEATURE = "feature"
    BUG = "bug"
    REFACTOR = "refactor"
    DOCUMENTATION = "documentation"
    TEST = "test"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class TaskRequest(BaseModel):
    id: str = Field(default_factory=lambda: f"task_{int(datetime.now().timestamp())}")
    type: TaskType = TaskType.FEATURE
    description: str
    context: Dict[str, Any] = Field(default_factory=dict)
    priority: Priority = Priority.MEDIUM
    created_at: datetime = Field(default_factory=datetime.now)

class ExecutionStep(BaseModel):
    step_num: int
    action: str
    target: str
    detail: str

class ExecutionPlan(BaseModel):
    task_id: str
    steps: List[ExecutionStep]

class CodeChange(BaseModel):
    file_path: str
    change_type: str
    diff: str

class Task(BaseModel):
    request: TaskRequest
    plan: Optional[ExecutionPlan] = None
    changes: List[CodeChange] = Field(default_factory=list)
