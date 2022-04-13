import typer
from .exporters import PrCommentsExporter

app = typer.Typer()

pr_comment_app = typer.Typer()

app.add_typer(pr_comment_app, name="pr-comment")


@pr_comment_app.command()
def list(repo: str):
    exporter = PrCommentsExporter(repo)
    exporter.print_as_csv()


if __name__ == "__main__":
    app()
