from dataclasses import dataclass


@dataclass
class ChannelStats:

    channel_id: int

    channel_name: str

    total_signals: int = 0

    winning_signals: int = 0

    losing_signals: int = 0

    ignored_signals: int = 0

    average_confidence: float = 0.0

    reliability: float = 50.0

    def record_signal(self, confidence):

        self.total_signals += 1

        self.average_confidence = (
            (
                self.average_confidence
                * (self.total_signals - 1)
            )
            + confidence
        ) / self.total_signals

    def record_win(self):

        self.winning_signals += 1
        self._update()

    def record_loss(self):

        self.losing_signals += 1
        self._update()

    def _update(self):

        trades = self.winning_signals + self.losing_signals

        if trades == 0:
            self.reliability = 50.0
            return

        self.reliability = round(
            (self.winning_signals / trades) * 100,
            2
        )