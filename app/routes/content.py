
from fastapi import APIRouter
from app.models.request_model import ContentRequest
from app.models.response_model import ContentResponse
from app.services.content_service import enhance_content

router = APIRouter()

@router.post("/enhance", response_model=ContentResponse)
def enhance(request: ContentRequest):

    result = enhance_content(
        request.context,
        request.platform
    )

    return ContentResponse(
        enhanced_content=result
    )