from fastapi import FastAPI

from api.routers import jobs


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(jobs.router)

    return app
