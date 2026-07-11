from core.ai_database import AIDatabase


db = AIDatabase()


def total_signals():

    row = db.cursor.execute(

        "SELECT COUNT(*) FROM signals"

    ).fetchone()

    return row[0]


def valid_signals():

    row = db.cursor.execute(

        """

        SELECT COUNT(*)

        FROM signals

        WHERE valid=1

        """

    ).fetchone()

    return row[0]