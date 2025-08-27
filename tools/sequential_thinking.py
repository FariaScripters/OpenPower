from src.mcp_server import Tool
from typing import Dict, Any, Optional
from pydantic import BaseModel

class SequentialThought(BaseModel):
    thought: str
    thought_number: int
    total_thoughts: int
    next_thought_needed: bool
    branch_from_thought: Optional[int] = None
    branch_id: Optional[str] = None
    is_revision: Optional[bool] = False
    needs_more_thoughts: Optional[bool] = False
    revises_thought: Optional[int] = None

class SequentialThinkingTool(Tool):
    def __init__(self):
        super().__init__(
            name="sequential-thinking",
            description="Dynamic and reflective problem-solving through thought sequences"
        )
        self.thoughts = []
        
    async def execute(self, params: Dict[str, Any]) -> Any:
        thought = SequentialThought(**params)
        
        # Store the thought in sequence
        if thought.thought_number <= len(self.thoughts):
            self.thoughts[thought.thought_number - 1] = thought
        else:
            self.thoughts.append(thought)
            
        response = {
            "thought_recorded": True,
            "current_sequence": len(self.thoughts),
            "thought": thought.dict()
        }
        
        # If this is a revision, include the original thought being revised
        if thought.is_revision and thought.revises_thought:
            original_thought = self.thoughts[thought.revises_thought - 1]
            response["original_thought"] = original_thought.dict()
            
        # If this branches from another thought, include the branch point
        if thought.branch_from_thought:
            branch_point = self.thoughts[thought.branch_from_thought - 1]
            response["branch_point"] = branch_point.dict()
            
        return response
