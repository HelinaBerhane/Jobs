import typer

cli = typer.Typer(
    add_completion=False,
)


@cli.command()
def main(name: str):
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    cli()
