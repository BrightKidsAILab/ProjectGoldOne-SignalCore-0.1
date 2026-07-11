from collections import Counter

_patterns = Counter()


def learn(signal):

    key = (

        signal.pair,

        signal.direction

    )

    _patterns[key] += 1


def frequency(pair, direction):

    return _patterns[(pair, direction)]