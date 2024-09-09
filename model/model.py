from pydantic import BaseModel
from typing import Optional

class SiteBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None

class Site(SiteBase):
    id: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Example Site",
                "description": "This is an example site.",
                "category": "Example Category",
                "id": "60c72b2f9b1e8a6c8e7f6e4d"
            }
        }
