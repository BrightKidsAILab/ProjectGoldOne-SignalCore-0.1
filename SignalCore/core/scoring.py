def score(signal):

    score = signal.confidence

    if signal.risk_reward:

        if signal.risk_reward >= 2:
            score += 15

        elif signal.risk_reward >= 1.5:
            score += 10

        elif signal.risk_reward >= 1:
            score += 5

    if len(signal.take_profits) >= 3:
        score += 5

    return min(score, 100)