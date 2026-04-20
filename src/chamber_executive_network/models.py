"""
Person and Executive Role Models
"""

from typing import Optional, List
from pydantic import BaseModel, Field

class ExecutiveRole(BaseModel):
    title: str = Field(..., description="Role title e.g. CEO, Director, President")
    company_siren: str = Field(..., description="Target company SIREN")
    company_name: str = Field(..., description="Target company name")
    start_date: Optional[str] = Field(None, description="ISO appointment date")

class PersonProfile(BaseModel):
    full_name: str = Field(..., description="Full legal name of executive")
    roles: List[ExecutiveRole] = Field(default_factory=list)
