class OrderExecutor:

    def execute(self, signal):

        print()

        print("ORDER EXECUTOR")

        print("----------------")

        print("PAIR :", signal.pair)

        print("SIDE :", signal.direction)

        print("ENTRY :", signal.entry)

        print("SL :", signal.stop_loss)

        print("TPS :", signal.take_profits)

        print()

        return True