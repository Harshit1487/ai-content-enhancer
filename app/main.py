
from fastapi import FastAPI
from app.routes.content import router as content_router
from app.routes.lead_scoring import router as lead_scoring_router

app = FastAPI()

app.include_router(content_router)
app.include_router(lead_scoring_router)

@app.get("/")
def health():
    return {"status": "UP"}
