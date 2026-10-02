from fastapi import FastAPI

from app.routes.documents import router as documents_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI is running"}


app.include_router(documents_router)