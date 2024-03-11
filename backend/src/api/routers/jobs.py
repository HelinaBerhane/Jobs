from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
def index():
    return {"Hello": "World"}
