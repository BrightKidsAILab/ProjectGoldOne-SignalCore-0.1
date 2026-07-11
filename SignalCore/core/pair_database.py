from core.ai_database import AIDatabase


db = AIDatabase()


def ranking():

    rows = db.cursor.execute(

        """

        SELECT

        pair,

        COUNT(*)

        FROM signals

        GROUP BY pair

        ORDER BY COUNT(*) DESC

        """

    ).fetchall()

    return rows