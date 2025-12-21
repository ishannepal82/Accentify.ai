import logging
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from src.config.Config import Config as ConfigClass

Config = ConfigClass()


async def init_db(app: FastAPI) -> None:
    """
    Initialize MongoDB and Redis clients and attach them to app.state
    """
    app.state.mongo_client = AsyncIOMotorClient(Config.mongo_uri)
    app.state.db = app.state.mongo_client.get_database()

    logging.info("MongoDB DB Initialized")


async def close_db(app: FastAPI) -> None:
    """
    Gracefully close MongoDB and Redis clients
    """
    if hasattr(app.state, "mongo_client"):
        app.state.mongo_client.close()

    logging.info("MongoDB and Redis closed")
