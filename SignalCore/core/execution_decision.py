from core.market_context import MarketContext


class ExecutionDecision:

    def __init__(self):

        self.market = MarketContext()

    def evaluate(self, signal):

        context = self.market.analyze(signal)

        decision = {

            "execute": True,

            "reason": "Approved",

            "context": context

        }

        if not context["tradable"]:

            decision["execute"] = False

            decision["reason"] = "Market Closed"

        elif signal.confidence < 70:

            decision["execute"] = False

            decision["reason"] = "Confidence Too Low"

        elif signal.conflict:

            decision["execute"] = False

            decision["reason"] = "Conflicting Signal"

        return decision