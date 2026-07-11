def quality(signal):

    score = 0

    if signal.pair:
        score += 20

    if signal.direction:
        score += 20

    if signal.entry:
        score += 20

    if signal.stop_loss:
        score += 20

    if signal.take_profits:

        score += 20

    return score