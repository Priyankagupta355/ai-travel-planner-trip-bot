from fastapi import FastAPI

from app.routes.auth import router as auth_router


app = FastAPI(
    title="AI Travel Planner",
    description="AI-powered travel planning chatbot",
    version="1.0.0"
)


app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "AI Travel Planner API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }