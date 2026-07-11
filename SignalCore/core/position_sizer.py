class PositionSizer:

    def calculate(

        self,

        balance,

        risk_percent,

        stop_loss_points

    ):

        if stop_loss_points <= 0:

            return 0.01

        risk = balance * (risk_percent / 100)

        lot = risk / stop_loss_points

        return round(max(0.01, lot), 2)