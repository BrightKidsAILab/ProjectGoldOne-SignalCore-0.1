import json
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "signals.jsonl")


def log_signal(signal):

    os.makedirs(LOG_DIR, exist_ok=True)

    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "pair": signal.pair,
        "direction": signal.direction,
        "entry": signal.entry,
        "stop_loss": signal.stop_loss,
        "take_profits": signal.take_profits,
        "confidence": signal.confidence,
        "risk_reward": signal.risk_reward,
        "valid": signal.valid,
        "errors": signal.errors,
        "source": signal.source,
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")