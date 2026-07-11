from core.logger import log
from core.health_check import run
from core.system_status import display


def initialize():

    log("========================================")

    log("ProjectGoldOne Starting")

    run()

    display()

    log("System Ready")

    log("========================================")