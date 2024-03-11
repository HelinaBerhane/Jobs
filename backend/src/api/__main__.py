import typer
import logging
import uvicorn
from typing_extensions import Annotated
from enum import Enum
from api.app import create_app

cli = typer.Typer(
    add_completion=False,
)


@cli.command()
def main(
    host: Annotated[
        str,
        typer.Option(help="Host to run the server on", envvar="HOST"),
    ] = "0.0.0.0",
    port: Annotated[
        int,
        typer.Option(help="Port to run the server on", envvar="PORT"),
    ] = 8000,
):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y %b %d, %H:%M",
        handlers=[
            logging.FileHandler("events.log"),
        ],
    )

    config = uvicorn.Config(
        create_app(),
        host=host,
        port=port,
        log_level="info",
    )

    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    cli()
