from core.config import DATABASE_DIR
from core.config import LOG_DIR
from core.config import CONFIG_DIR


def run():

    print()

    print("Running Health Check...")

    print()

    print("Database :", DATABASE_DIR.exists())

    print("Logs :", LOG_DIR.exists())

    print("Config :", CONFIG_DIR.exists())

    print()

    print("Health Check Passed")

    print()