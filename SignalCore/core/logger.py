from datetime import datetime
from core.config import LOG_DIR


LOG_FILE = LOG_DIR / "system.log"


def log(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{timestamp}] {message}"

    print(line)

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        f.write(line + "\n")