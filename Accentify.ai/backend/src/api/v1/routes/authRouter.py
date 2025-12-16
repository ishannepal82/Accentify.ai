from fastapi import APIRouter

authRouter = APIRouter()

@authRouter.post("/login")
async def login():
    return {"message": "Login"}

@authRouter.post("/register")
async def register():
    return {"message": "Register"}

@authRouter.post("/logout")
async def logout():
    return {"message": "Logout"}