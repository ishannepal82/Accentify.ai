from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.tests.routes import test_router
from src.config.Config import Config as ConfigClass
from src.config.db import init_db, close_db
from src.config.redis import init_redis, close_redis
from src.middlewares.cors import setup_cors

Config = ConfigClass()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Accentify.ai Backend",
        description="Backend API for Accent Detector and AI Conversations",
        version="0.1.0",
    )

     # Setup CORS
    setup_cors(app)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Initialize MongoDB
        await init_db(app)
        # Initialize Redis
        await init_redis(app)

        yield
        # Close MongoDB
        await close_db(app)
        # Close Redis
        await close_redis(app)

    app.router.lifespan_context = lifespan

    app.include_router(test_router)
    return app
