from datetime import datetime


class SessionFilter:

    def current_session(self):

        hour = datetime.utcnow().hour

        if 0 <= hour < 7:
            return "ASIAN"

        if 7 <= hour < 13:
            return "LONDON"

        if 13 <= hour < 21:
            return "NEW_YORK"

        return "SYDNEY"

    def tradable(self):

        session = self.current_session()

        return session != "SYDNEY"