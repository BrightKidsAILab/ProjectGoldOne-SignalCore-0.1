class OrderManager:

    def modify_sl(self, trade, price):

        print(

            "Move SL",

            trade.pair,

            price

        )

    def modify_tp(self, trade, price):

        print(

            "Move TP",

            trade.pair,

            price

        )

    def close(self, trade):

        print(

            "Closing",

            trade.pair

        )