import json
import logging

import typer
import uvicorn
from api.server import create_server
from databases import Database
from fastapi.openapi.utils import get_openapi
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def serve(
    host: Annotated[
        str,
        typer.Option(help="Host to run the server on", envvar="HOST"),
    ] = "0.0.0.0",
    port: Annotated[
        int,
        typer.Option(help="Port to run the server on", envvar="PORT"),
    ] = 8000,
    database_url: Annotated[
        str,
        typer.Option(help="Database URL", envvar="DATABASE_URL"),
    ] = "sqlite+aiosqlite:///db.sqlite3",
):
    # TODO: consider moving the log level to a command line argument
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y %b %d, %H:%M",
        handlers=[
            logging.FileHandler("events.log"),
        ],
    )

    database = Database(database_url)

    server = create_server(database)

    uvicorn.run(
        server,
        host=host,
        port=port,
    )


@app.command()
def generate_openapi(
    output: Annotated[
        str,
        typer.Option(help="Location to output openapi json spec", envvar="?"),
    ] = "openapi.json",
):
    dummy_database_url = "sqlite+aiosqlite:///db.sqlite3"
    database = Database(dummy_database_url)

    # this is only used to get information about the server structure
    dummy_server = create_server(database)

    with open(output, "w") as f:
        json.dump(
            get_openapi(
                title=dummy_server.title,
                version=dummy_server.version,
                openapi_version=dummy_server.openapi_version,
                description=dummy_server.description,
                routes=dummy_server.routes,
            ),
            f,
        )


if __name__ == "__main__":
    app()
