from pathlib import Path

from typer import Option
from typer.main import get_command, Typer

app = Typer(add_completion=False)


@app.command()
def some_prog(some_path: Path = Option(Path("/this/is/a/path"), help="This uses a pathlib.Path")):
    """Bad default for --some-path."""

    pass


typer_click_object = get_command(app)
