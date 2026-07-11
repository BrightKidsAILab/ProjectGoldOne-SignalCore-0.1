def fuse(signals):

    if not signals:

        return None

    best = max(

        signals,

        key=lambda s: s.confidence

    )

    return best