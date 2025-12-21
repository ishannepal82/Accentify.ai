import redis.asyncio as redis
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from src.config.Config import Config as ConfigClass

Config = ConfigClass()

async def init_redis(app: FastAPI) -> None:
    """
    Initialize Redis client and attach it to app.state
    """
    app.state.redis = redis.Redis.from_url(
        Config.redis_uri,
        decode_responses=True,
    )

    logging.info("Redis Initialized")

async def close_redis(app: FastAPI) -> None:
    """
    Gracefully close Redis client
    """
    if hasattr(app.state, "redis"):
        await app.state.redis.close()

    logging.info("Redis closed")