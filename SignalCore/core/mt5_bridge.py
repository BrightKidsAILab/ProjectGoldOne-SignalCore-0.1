from core.broker_adapter import BrokerAdapter
from core.account_monitor import AccountMonitor
from core.order_executor import OrderExecutor
from core.order_manager import OrderManager


class MT5Bridge:

    def __init__(self):

        self.broker = BrokerAdapter()

        self.account = AccountMonitor()

        self.executor = OrderExecutor()

        self.orders = OrderManager()

    def send(self, signal):

        if not self.broker.connected():

            print("Broker offline.")

            return False

        if not self.account.healthy():

            print("Account unhealthy.")

            return False

        return self.executor.execute(signal)