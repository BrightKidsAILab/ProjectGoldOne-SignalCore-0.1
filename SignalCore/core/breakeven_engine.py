class BreakEvenEngine:

    def update(self, trade):

        if not hasattr(trade, "breakeven"):

            trade.breakeven = False

        if trade.breakeven:

            return

        # MT5 Bridge will move SL later

        if trade.risk_reward is not None:

            if trade.risk_reward >= 1:

                trade.breakeven = True

                print("Break-even activated:", trade.pair)