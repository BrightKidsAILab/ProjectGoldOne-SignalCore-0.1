from collections import defaultdict

_consensus = defaultdict(list)


def register(signal):

    key = signal.pair

    _consensus[key].append(signal)

    return len(_consensus[key])


def get(pair):

    return _consensus.get(pair, [])