from databases import Database
from fastapi import FastAPI

from api.db import init_db
from api.routers import hello_router


def create_server(database: Database) -> FastAPI:
    """
    Creates the FastAPI server instance.

    Args:
        database (Database): The database instance.

    Returns:
        FastAPI: The FastAPI server instance.
    """
    init_db(database)

    app = FastAPI()

    app.include_router(hello_router)

    return app
