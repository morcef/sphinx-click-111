import pathlib

import click


@click.command()
@click.option('--some-path', default=pathlib.Path("/this/is/a/path"), type=click.Path(path_type=pathlib.Path), help='This uses a click.Path')
def click_prog(some_path):
    """Bad default for --some-path."""

    pass
