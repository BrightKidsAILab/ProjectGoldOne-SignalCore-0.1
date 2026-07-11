from collections import defaultdict


_database = defaultdict(list)


def save(category, data):

    _database[category].append(data)


def load(category):

    return _database.get(category, [])


def count(category):

    return len(load(category))