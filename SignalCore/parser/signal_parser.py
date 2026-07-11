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
    "US100": "NAS100",
    "US30": "US30",
    "EURUSD": "EURUSD",
    "GBPUSD": "GBPUSD",
    "USDJPY": "USDJPY",
}


def detect_pair(text):
    for alias, symbol in PAIR_ALIASES.items():
        pattern = rf"\b{re.escape(alias)}\b"

        if re.search(pattern, text):
            
            return symbol

    return None


def detect_direction(text):

    patterns = [
        ("BUY LIMIT", "BUY LIMIT"),
        ("SELL LIMIT", "SELL LIMIT"),
        ("BUY STOP", "BUY STOP"),
        ("SELL STOP", "SELL STOP"),
        ("BUY", "BUY"),
        ("SELL", "SELL"),
    ]

    for keyword, value in patterns:
        if re.search(rf"\b{keyword}\b", text):
            return value

    return None


def detect_entry(text):

    patterns = [
        r"ENTRY\s*[:=@]?\s*([\d.]+)",
        r"ENTRY PRICE\s*[:=@]?\s*([\d.]+)",
        r"@\s*([\d.]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return float(match.group(1))

    match = re.search(
        r"(BUY|SELL)\s+[A-Z0-9]+\s+([\d.]+)\s*-\s*([\d.]+)",
        text
    )

    if match:
        return round(
            (float(match.group(2)) + float(match.group(3))) / 2,
            2
        )

    match = re.search(
        r"(BUY|SELL)\s+[A-Z0-9]+\s+([\d.]+)",
        text
    )

    if match:
        return float(match.group(2))

    return None


def detect_stoploss(text):

    match = re.search(
        r"(SL|STOP LOSS|STOPLOSS|S/L)\s*[:=@]?\s*([\d.]+)",
        text
    )

    if match:
        return float(match.group(2))

    return None


def detect_takeprofits(text):

    tps = []

    matches = re.findall(
        r"(?:TP|TARGET)\d*\s*[:=@]?\s*([\d.]+)",
        text
    )

    for tp in matches:
        value = float(tp)
        if value not in tps:
            tps.append(value)

    match = re.search(
        r"(?:TP|TARGET)\s+((?:[\d.]+\s*)+)",
        text
    )

    if match:
        for value in match.group(1).split():
            value = float(value)
            if value not in tps:
                tps.append(value)

    return tps


def parse_signal(message):

    text = message.upper()

    return {
        "pair": detect_pair(text),
        "direction": detect_direction(text),
        "entry": detect_entry(text),
        "stop_loss": detect_stoploss(text),
        "take_profits": detect_takeprofits(text),
    }