"""fossil log — record a new decision."""

import uuid
from datetime import datetime, timezone

import click

from fossil.db import get_connection


@click.command("log")
@click.argument("description")
@click.option(
    "--prediction",
    default=None,
    help="Your expected outcome for this decision.",
)
@click.option(
    "--confidence",
    default=None,
    type=click.IntRange(0, 100),
    help="How confident you are in your prediction (0-100).",
)
def log(description: str, prediction: str | None, confidence: int | None) -> None:
    """Log a new decision DESCRIPTION to the journal."""
    if confidence is not None and prediction is None:
        raise click.UsageError("--confidence requires --prediction to be set.")

    decision_id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc).isoformat()

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO decisions (id, created_at, description, prediction, confidence)
            VALUES (?, ?, ?, ?, ?)
            """,
            (decision_id, created_at, description, prediction, confidence),
        )
        conn.commit()

    click.echo(f"Decision logged with ID: {decision_id}")
    click.echo(f"Timestamp  : {created_at}")
    click.echo(f"Description: {description}")
    if prediction is not None:
        click.echo(f"Prediction : {prediction}")
    if confidence is not None:
        click.echo(f"Confidence : {confidence}%")
