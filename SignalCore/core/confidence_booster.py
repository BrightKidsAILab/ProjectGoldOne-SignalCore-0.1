def boost(signal, cluster):

    if cluster["buy"] >= 3 and signal.direction == "BUY":
        signal.confidence += 10

    elif cluster["sell"] >= 3 and signal.direction == "SELL":
        signal.confidence += 10

    signal.confidence = min(signal.confidence, 100)

    return signal