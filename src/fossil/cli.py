"""Entry-point for the Fossil CLI."""

import click

from fossil.commands.log import log


@click.group()
def main() -> None:
    """Fossil — your personal decision journal."""


main.add_command(log)
