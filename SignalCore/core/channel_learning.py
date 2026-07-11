from core.channel_profiler import update
from core.reputation_engine import reputation


def learn(signal):

    update(signal)

    rep = reputation(signal.source)

    print()

    print("========== CHANNEL AI ==========")

    print("Source :", signal.source)

    print("Reputation :", rep)

    if rep >= 90:

        print("⭐⭐⭐⭐⭐ Elite Channel")

    elif rep >= 75:

        print("⭐⭐⭐⭐ Trusted")

    elif rep >= 60:

        print("⭐⭐⭐ Average")

    elif rep >= 40:

        print("⭐⭐ Weak")

    else:

        print("⭐ Dangerous")

    print("===============================")