from fastapi import FastAPI
from src.presentation.api.user_router import router

app = FastAPI(title="Senior Structured API")

app.include_router(router)