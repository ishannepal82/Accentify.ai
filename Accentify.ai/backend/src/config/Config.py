import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

class Config:
    mongo_uri: str = os.getenv("MONGO_URI", "mongodb://localhost:27017/accentify.ai")
    redis_uri: str = os.getenv("REDIS_URI", "redis://localhost:6379")

if not Config.mongo_uri or not Config.redis_uri:
    raise RuntimeError("Missing required environment variables")