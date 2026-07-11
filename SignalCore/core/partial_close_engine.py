class PartialCloseEngine:

    def update(self, trade):

        if not hasattr(trade, "partial_closed"):

            trade.partial_closed = False

        if trade.partial_closed:

            return

        if len(trade.take_profits) >= 2:

            trade.partial_closed = True

            print(

                "Partial close prepared:",

                trade.pair

            )