_whitelist = set()


def add(source):

    _whitelist.add(source)


def trusted(source):

    return source in _whitelist