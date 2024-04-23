from api.db import init_db
from api.routers import jobs_router
from databases import Database
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware


def use_route_names_as_operation_ids(app: FastAPI):
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


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

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # TODO: Configurable
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(jobs_router)

    use_route_names_as_operation_ids(app)

    return app
