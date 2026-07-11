from core.channel_profiler import profile


def reputation(source):

    p = profile(source)

    if p is None:
        return 50

    if p["signals"] == 0:
        return 50

    valid_rate = (

        p["valid"] /

        p["signals"]

    ) * 100

    avg_confidence = (

        p["confidence"] /

        p["signals"]

    )

    return round(

        (valid_rate * 0.6) +

        (avg_confidence * 0.4),

        2

    )