from datetime import datetime, timedelta

_recent_signals = {}


def _signal_key(signal):
    return (
        signal.pair,
        signal.direction,
        signal.entry,
        signal.stop_loss,
        tuple(signal.take_profits)
    )


def is_duplicate(signal, expiry_seconds=300):

    now = datetime.utcnow()

    key = _signal_key(signal)

    expired = []

    for k, t in _recent_signals.items():
        if now - t > timedelta(seconds=expiry_seconds):
            expired.append(k)

    for k in expired:
        del _recent_signals[k]

    if key in _recent_signals:
        return True

    _recent_signals[key] = now

    return False