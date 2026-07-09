import re


PAIR_ALIASES = {
    "GOLD": "XAUUSD",
    "XAU": "XAUUSD",
    "XAUUSD": "XAUUSD",
    "BTC": "BTCUSD",
    "BTCUSD": "BTCUSD",
    "ETH": "ETHUSD",
    "ETHUSD": "ETHUSD",
    "NAS100": "NAS100",
    "US30": "US30",
    "EURUSD": "EURUSD",
    "GBPUSD": "GBPUSD",
    "USDJPY": "USDJPY",
}


def detect_pair(text):
    for alias, symbol in PAIR_ALIASES.items():
        if alias in text:
            return symbol
    return None


def detect_entry(text):
    # Entry: 3345
    match = re.search(r"ENTRY[: ]+([\d.]+)", text)
    if match:
        return float(match.group(1))

    # BUY GOLD 4110-4108
    match = re.search(r"(BUY|SELL)\s+[A-Z0-9]+\s+([\d.]+)\s*-\s*([\d.]+)", text)
    if match:
        price1 = float(match.group(2))
        price2 = float(match.group(3))
        return (price1 + price2) / 2

    return None


def detect_stoploss(text):
    match = re.search(r"(SL|STOP LOSS|STOPLOSS|S/L)[: ]+([\d.]+)", text)
    if match:
        return float(match.group(2))
    return None


def detect_takeprofits(text):
    values = []

    # TP1, TP2, TP3...
    matches = re.findall(r"TP\d*[: ]+([\d.]+)", text)
    values.extend(matches)

    # TP 4112 4115 4120
    match = re.search(r"TP\s+((?:[\d.]+\s*)+)", text)

    if match:
        values.extend(match.group(1).split())

    return [float(x) for x in values]


def parse_signal(message):

    text = message.upper()

    signal = {
        "pair": detect_pair(text),
        "direction": "BUY" if "BUY" in text else "SELL" if "SELL" in text else None,
        "entry": detect_entry(text),
        "stop_loss": detect_stoploss(text),
        "take_profits": detect_takeprofits(text),
    }

    return signal