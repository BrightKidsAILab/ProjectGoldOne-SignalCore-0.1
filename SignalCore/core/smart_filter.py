from core.consensus_engine import register
from core.signal_cluster import cluster
from core.confidence_booster import boost
from core.fake_signal_detector import suspicious


def filter_signal(signal):

    register(signal)

    info = cluster(signal)

    signal = boost(signal, info)

    if suspicious(signal):

        signal.valid = False

        signal.errors.append("Rejected by Smart Filter")

    return signal