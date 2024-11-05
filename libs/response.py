from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class ResponseDict(dict):
     def __init__(self, success: bool, message: str, data: Dict[str, Any], errors: Optional[Dict[str, Any]] = None):
        super().__init__(success=success, message=message, data=data, errors=errors)

    
