from fastapi import APIRouter, Request

test_router = APIRouter()

@test_router.get("/test", tags=["Test"])
async def test_endpoint(request: Request):
    await request.app.state.db.command("ping")
    await request.app.state.redis.ping()

    return {"message": "Test endpoint is working!"}
