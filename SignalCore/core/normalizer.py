from core.models import Signal


def normalize(parsed_signal):

    signal = Signal()

    signal.pair = parsed_signal.get("pair")
    signal.direction = parsed_signal.get("direction")

    signal.entry = parsed_signal.get("entry")
    signal.stop_loss = parsed_signal.get("stop_loss")

    signal.take_profits = parsed_signal.get(
        "take_profits",
        []
    )

    return signal