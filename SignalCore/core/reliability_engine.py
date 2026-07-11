from core.history import get_stats


def reliability(source):

    stats = get_stats(source)

    wins = stats["wins"]
    losses = stats["losses"]

    total = wins + losses

    if total == 0:
        return 50.0

    return round((wins / total) * 100, 2)