from core.market_memory import remember as remember_market
from core.pattern_memory import learn
from core.ai_memory import remember


class AIDecision:

    def evaluate(self, signal):

        remember_market(signal)

        learn(signal)

        remember(signal)

        return signal