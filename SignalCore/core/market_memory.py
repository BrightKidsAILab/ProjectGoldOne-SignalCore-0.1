from core.learning_database import save, load


def remember(signal):

    save("market", {

        "pair": signal.pair,

        "direction": signal.direction,

        "confidence": signal.confidence,

        "source": signal.source

    })


def history():

    return load("market")