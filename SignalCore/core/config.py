from pathlib import Path


# ===============================
# PATHS
# ===============================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"

LOG_DIR = BASE_DIR / "logs"

CONFIG_DIR = BASE_DIR / "config"

DATABASE_DIR.mkdir(exist_ok=True)

LOG_DIR.mkdir(exist_ok=True)

CONFIG_DIR.mkdir(exist_ok=True)


# ===============================
# SIGNAL SETTINGS
# ===============================

MIN_CONFIDENCE = 70

MAX_OPEN_TRADES = 5

MAX_DAILY_LOSS = 5.0

DEFAULT_RISK = 1.0


# ===============================
# AI SETTINGS
# ===============================

CONSENSUS_REQUIRED = 3

PATTERN_BONUS = 5

REPUTATION_ELITE = 90

REPUTATION_TRUSTED = 75


# ===============================
# DATABASE
# ===============================

DATABASE_FILE = DATABASE_DIR / "projectgoldone.db"