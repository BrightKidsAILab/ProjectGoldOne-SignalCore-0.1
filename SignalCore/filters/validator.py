def calculate_rr(signal):
    if (
        signal.entry is None
        or signal.stop_loss is None
        or len(signal.take_profits) == 0
    ):
        return None

    risk = abs(signal.entry - signal.stop_loss)

    if risk == 0:
        return None

    reward = abs(signal.take_profits[0] - signal.entry)

    return round(reward / risk, 2)


def validate_signal(signal):

    signal.errors = []
    signal.confidence = 0

    if signal.pair:
        signal.confidence += 20
    else:
        signal.errors.append("Missing trading pair")

    if signal.direction:
        signal.confidence += 20
    else:
        signal.errors.append("Missing direction")

    if signal.entry is not None:
        signal.confidence += 20
    else:
        signal.errors.append("Missing entry")

    if signal.stop_loss is not None:
        signal.confidence += 20
    else:
        signal.errors.append("Missing stop loss")

    if len(signal.take_profits) > 0:
        signal.confidence += 20
    else:
        signal.errors.append("Missing take profit")

    signal.risk_reward = calculate_rr(signal)

    signal.valid = signal.confidence >= 80

    return signal