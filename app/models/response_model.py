from pydantic import BaseModel

class ContentResponse(BaseModel):
    enhanced_content: str