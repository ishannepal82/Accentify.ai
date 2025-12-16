from fastapi import FastAPI
from src.api.v1.routes.authRouter import authRouter

def create_app():
    app = FastAPI()

    @app.get("/")
    def root():
        return {"message": "Hello World"}
    
    app.include_router(authRouter, prefix="/api/v1/auth")
    return app