from core.trend_engine import TrendEngine
from core.volatility_filter import VolatilityFilter
from core.session_filter import SessionFilter


class MarketContext:

    def __init__(self):

        self.trend = TrendEngine()

        self.volatility = VolatilityFilter()

        self.session = SessionFilter()

    def analyze(self, signal):

        return {

            "trend": self.trend.analyze(signal),

            "volatility": self.volatility.analyze(),

            "session": self.session.current_session(),

            "tradable": self.session.tradable()

        }