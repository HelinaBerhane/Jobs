from databases import Database
from fastapi import FastAPI

from api.db import init_db
from api.routers import jobs


def create_app(database: Database) -> FastAPI:
    """
    Creates the FastAPI application with a global database.

    Args:
        database (Database): The database instance.

    Returns:
        FastAPI: The FastAPI application.
    """
    app = FastAPI()

    init_db(database)

    app.include_router(jobs.router)

    return app
