import logging
import asyncio
import typer
import uvicorn
from api.server import create_server
from databases import Database
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

    uvicorn.run(server, host=host, port=port)


# TODO: Move this to a separate module with a proper migration system
async def run_migrations(database: Database) -> None:
    migrations = [
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            created_date TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """,
    ]

    for migration in migrations:
        await database.execute(migration)


@app.command()
def migrate(
    database_url: Annotated[
        str,
        typer.Option(help="Database URL", envvar="DATABASE_URL"),
    ] = "sqlite+aiosqlite:///db.sqlite3",
):
    database = Database(database_url)

    asyncio.run(run_migrations(database))


if __name__ == "__main__":
    app()
