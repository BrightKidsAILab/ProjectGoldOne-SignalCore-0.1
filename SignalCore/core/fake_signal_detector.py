def suspicious(signal):

    if signal.entry is None:
        return True

    if signal.stop_loss is None:
        return True

    if len(signal.take_profits) == 0:
        return True

    if signal.risk_reward is not None:

        if signal.risk_reward < 0.30:
            return True

    return False