_active = {}


def _key(signal):

    return (

        signal.source,

        signal.pair,

        signal.entry

    )


def add(signal):

    _active[_key(signal)] = signal


def remove(signal):

    _active.pop(_key(signal), None)


def active():

    return list(_active.values())


def find(pair):

    for signal in _active.values():

        if signal.pair == pair:

            return signal

    return None


def exists(signal):

    return _key(signal) in _active


def count():

    return len(_active)