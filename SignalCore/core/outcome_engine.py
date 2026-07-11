from core.history import record_result
from core.trade_tracker import remove


def mark_win(signal):

    record_result(signal.source, True)

    remove(signal)


def mark_loss(signal):

    record_result(signal.source, False)

    remove(signal)