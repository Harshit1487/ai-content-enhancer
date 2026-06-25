from pydantic import BaseModel

class ContentRequest(BaseModel):
    context: str
    platform: str