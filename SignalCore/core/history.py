from collections import defaultdict

_channel_stats = defaultdict(
    lambda: {
        "signals": 0,
        "wins": 0,
        "losses": 0,
        "confidence": []
    }
)


def record_signal(signal):

    stats = _channel_stats[signal.source]

    stats["signals"] += 1
    stats["confidence"].append(signal.confidence)


def record_result(source, win):

    stats = _channel_stats[source]

    if win:
        stats["wins"] += 1
    else:
        stats["losses"] += 1


def get_stats(source):

    return _channel_stats[source]