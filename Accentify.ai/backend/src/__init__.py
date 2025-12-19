from redis.asyncio import Redis
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from src.config.Config import Config as ConfigClass

Config = ConfigClass()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Accentify.ai Backend",
        description="Backend API for Accent Detector and AI Conversations",
        version="0.1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.mongo_client = AsyncIOMotorClient(Config.mongo_uri)
        app.state.mongodb = app.state.mongo_client.get_database()
        app.state.redis = Redis.from_url(
        Config.redis_uri,
        decode_responses=True,
        )
        logging.info("MongoDB and Redis clients initialized")
        yield
        app.state.mongo_client.close()
        await app.state.redis.close()
        logging.info("MongoDB and Redis clients closed")

    app.router.lifespan_context = lifespan

    @app.get("/health", tags=["Health"])
    async def health_check():
        mongo_ping = await app.state.mongodb.command("ping")
        redis_ping = await app.state.redis.ping()
        return {
            "status": "ok",
            "mongo": mongo_ping,
            "redis": redis_ping,
        }

    return app
