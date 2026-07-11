class TrailingStopEngine:

    def update(self, trade):

        if not hasattr(trade, "trail_count"):

            trade.trail_count = 0

        trade.trail_count += 1

        print(

            "Trailing",

            trade.pair,

            "#",

            trade.trail_count

        )