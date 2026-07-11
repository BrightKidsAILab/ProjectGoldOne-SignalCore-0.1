from core.reliability_engine import reliability

_rank_cache = {}


def update(source):

    score = reliability(source)

    _rank_cache[source] = score

    return score


def ranking():

    return sorted(
        _rank_cache.items(),
        key=lambda x: x[1],
        reverse=True
    )