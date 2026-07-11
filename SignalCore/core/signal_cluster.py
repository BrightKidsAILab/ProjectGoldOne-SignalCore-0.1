from core.consensus_engine import get


def cluster(signal):

    signals = get(signal.pair)

    buy = 0
    sell = 0

    for s in signals:

        if s.direction == "BUY":
            buy += 1
        elif s.direction == "SELL":
            sell += 1

    return {
        "buy": buy,
        "sell": sell,
        "total": len(signals)
    }