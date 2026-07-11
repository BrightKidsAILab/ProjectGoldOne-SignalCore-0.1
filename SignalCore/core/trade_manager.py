from core.position_manager import PositionManager
from core.breakeven_engine import BreakEvenEngine
from core.trailing_stop_engine import TrailingStopEngine
from core.partial_close_engine import PartialCloseEngine


class TradeManager:

    def __init__(self):

        self.positions = PositionManager()
        self.breakeven = BreakEvenEngine()
        self.trailing = TrailingStopEngine()
        self.partial = PartialCloseEngine()

    def manage(self):

        positions = self.positions.open_positions()

        for position in positions:

            self.breakeven.update(position)

            self.trailing.update(position)

            self.partial.update(position)