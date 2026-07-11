from core.ai_statistics import total_signals
from core.ai_statistics import valid_signals


def display():

    total = total_signals()

    valid = valid_signals()

    print()

    print("========== SYSTEM STATUS ==========")

    print("Signals Learned :", total)

    print("Valid Signals   :", valid)

    print("===================================")

    print()