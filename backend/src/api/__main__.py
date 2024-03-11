import asyncio
import logging

import typer
import uvicorn
from api.app import create_app
from databases import Database
from repositories.jobs import JobsRepository
from typing_extensions import Annotated

cli = typer.Typer(
    add_completion=False,
)


@cli.command()
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
    """
    Run the jobs api server.
    """
    database = Database(database_url)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y %b %d, %H:%M",
        handlers=[
            logging.FileHandler("events.log"),
        ],
    )

    config = uvicorn.Config(
        create_app(database),
        host=host,
        port=port,
        log_level="info",
    )

    server = uvicorn.Server(config)
    server.run()


async def run_migrations(database: Database):
    """
    Run the database migrations.

    Args:
        database (Database): The database instance.
    """
    jobs_repository = JobsRepository(database)
    print("Creating jobs table...")
    await jobs_repository.create_table()
    print("done")


@cli.command()
def migrate(
    database_url: Annotated[
        str,
        typer.Option(help="Database URL", envvar="DATABASE_URL"),
    ] = "sqlite+aiosqlite:///db.sqlite3",
):
    """
    Run the database migrations.
    """

    asyncio.run(run_migrations(Database(database_url)))


if __name__ == "__main__":
    cli()
