"""Database initialisation and connection helpers."""

import sqlite3
from pathlib import Path

DB_PATH = Path.home() / ".fossil" / "fossil.db"


def get_connection() -> sqlite3.Connection:
    """Return a connection to the Fossil SQLite database, creating it if needed."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _init_schema(conn)
    return conn


def _init_schema(conn: sqlite3.Connection) -> None:
    """Create tables if they do not yet exist."""
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS decisions (
            id          TEXT PRIMARY KEY,
            created_at  TEXT NOT NULL,
            description TEXT NOT NULL,
            prediction  TEXT,
            confidence  INTEGER,
            outcome     TEXT,
            correct     INTEGER
        );
        """
    )
    conn.commit()
