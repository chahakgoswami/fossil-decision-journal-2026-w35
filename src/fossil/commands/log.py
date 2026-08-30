"""fossil log — record a new decision."""

import uuid
from datetime import datetime, timezone

import click

from fossil.db import get_connection


@click.command("log")
@click.argument("description")
def log(description: str) -> None:
    """Log a new decision DESCRIPTION to the journal."""
    decision_id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc).isoformat()

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO decisions (id, created_at, description)
            VALUES (?, ?, ?)
            """,
            (decision_id, created_at, description),
        )
        conn.commit()

    click.echo(f"Decision logged with ID: {decision_id}")
    click.echo(f"Timestamp : {created_at}")
    click.echo(f"Description: {description}")
