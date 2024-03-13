from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
)

router.get("/")


@router.get("/")
async def hello():
    return {"message": "Hello, world!"}
