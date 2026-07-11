from core.position_sizer import PositionSizer
from core.exposure_manager import ExposureManager
from core.daily_guard import DailyGuard
from core.account_protector import AccountProtector


class RiskManager:

    def __init__(self):

        self.position = PositionSizer()
        self.exposure = ExposureManager()
        self.daily = DailyGuard()
        self.protector = AccountProtector()

    def approve(self, signal):

        if not self.daily.can_trade():

            return False, "Daily trading stopped"

        if not self.exposure.can_open(signal):

            return False, "Exposure exceeded"

        if not self.protector.account_safe():

            return False, "Account protection active"

        return True, "Approved"