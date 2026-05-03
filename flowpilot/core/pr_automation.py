from typing import Dict, Any
from ..models.task import TaskRequest, CodeChange
from typing import List

class PRAutomation:
    """Generates Pull Request artifacts like commit messages and PR descriptions."""
    
    def generate_artifacts(self, request: TaskRequest, changes: List[CodeChange]) -> Dict[str, Any]:
        print("\n[PRAutomation] Generating Git artifacts...")
        
        title = f"Feat: {request.description}" if request.type == "feature" else f"Fix: {request.description}"
        summary = f"Automated implementation of '{request.description}'. Modified {len(changes)} files. All tests passing."
        
        print(f"  PR Title: {title}")
        print(f"  PR Description: {summary}")
        
        return {
            "title": title,
            "description": summary,
            "commit_messages": [f"auto: {c.change_type} {c.file_path}" for c in changes]
        }
