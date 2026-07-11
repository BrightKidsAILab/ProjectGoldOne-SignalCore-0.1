from collections import deque

signals = deque(maxlen=500)


def remember(signal):

    signals.append(signal)


def recent():

    return list(signals)