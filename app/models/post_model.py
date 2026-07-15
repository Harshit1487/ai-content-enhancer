from pydantic import BaseModel


class PublishPostRequest(BaseModel):
    text: str