class AccountMonitor:

    def info(self):

        return {

            "balance": 0,

            "equity": 0,

            "margin": 0,

            "free_margin": 0

        }

    def healthy(self):

        account = self.info()

        return account["free_margin"] >= 0