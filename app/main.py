
from fastapi import FastAPI
from app.routes.content import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def health():
    return {"status": "UP"}