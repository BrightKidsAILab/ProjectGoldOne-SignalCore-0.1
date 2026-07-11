from core.ai_database import AIDatabase


db = AIDatabase()


def ranking():

    rows = db.cursor.execute(

        """

        SELECT

        source,

        COUNT(*),

        AVG(confidence)

        FROM signals

        GROUP BY source

        ORDER BY AVG(confidence) DESC

        """

    ).fetchall()

    return rows