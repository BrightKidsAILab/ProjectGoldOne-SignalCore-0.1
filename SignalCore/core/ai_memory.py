from core.ai_database import AIDatabase


db = AIDatabase()


def remember(signal):

    db.cursor.execute(

        """

        INSERT INTO signals(

            pair,

            direction,

            confidence,

            source,

            valid

        )

        VALUES(?,?,?,?,?)

        """,

        (

            signal.pair,

            signal.direction,

            signal.confidence,

            signal.source,

            int(signal.valid)

        )

    )

    db.conn.commit()