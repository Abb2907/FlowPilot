import json
from typing import Dict, Any
from ..models.task import TaskRequest, TaskType, Priority

class InputHandler:
    """Handles parsing and normalizing input tickets, PRs, or natural language."""
    
    def process_input(self, text: str, input_type: str = "natural") -> TaskRequest:
        print(f"[InputHandler] Processing {input_type} input...")
        
        # Heuristic parsing for PoC
        task_type = TaskType.FEATURE
        priority = Priority.MEDIUM
        
        text_lower = text.lower()
        if "fix" in text_lower or "bug" in text_lower:
            task_type = TaskType.BUG
        elif "refactor" in text_lower:
            task_type = TaskType.REFACTOR
            
        if "urgent" in text_lower or "critical" in text_lower:
            priority = Priority.CRITICAL
            
        return TaskRequest(
            type=task_type,
            description=text,
            priority=priority
        )
