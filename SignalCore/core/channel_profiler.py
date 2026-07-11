_profiles = {}


def update(signal):

    source = signal.source

    if source not in _profiles:

        _profiles[source] = {

            "signals": 0,
            "valid": 0,
            "confidence": 0

        }

    p = _profiles[source]

    p["signals"] += 1

    if signal.valid:
        p["valid"] += 1

    p["confidence"] += signal.confidence


def profile(source):

    return _profiles.get(source)