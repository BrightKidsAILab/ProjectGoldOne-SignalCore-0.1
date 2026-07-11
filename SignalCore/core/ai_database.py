import sqlite3
from pathlib import Path


DB_PATH = Path("database")

DB_PATH.mkdir(exist_ok=True)

DATABASE = DB_PATH / "projectgoldone.db"


class AIDatabase:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)

        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS signals(

            id INTEGER PRIMARY KEY,

            pair TEXT,

            direction TEXT,

            confidence REAL,

            source TEXT,

            valid INTEGER,

            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        self.conn.commit()