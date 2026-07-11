_recent = {}


def has_conflict(signal):

    pair = signal.pair

    if pair not in _recent:
        _recent[pair] = signal
        return False

    previous = _recent[pair]

    if previous.direction != signal.direction:

        _recent[pair] = signal

        return True

    _recent[pair] = signal

    return False