_blacklist = set()


def add(source):

    _blacklist.add(source)


def blocked(source):

    return source in _blacklist