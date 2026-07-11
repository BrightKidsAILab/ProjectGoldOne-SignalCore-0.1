from core.scoring import score
from core.conflict_detector import has_conflict
from core.signal_memory import remember
from core.history import record_signal

from core.smart_filter import filter_signal
from core.execution_decision import ExecutionDecision
from core.ai_decision import AIDecision


decision_engine = ExecutionDecision()
ai_engine = AIDecision()


def process(signal):

    signal.confidence = score(signal)

    signal.conflict = has_conflict(signal)

    remember(signal)

    record_signal(signal)

    signal = filter_signal(signal)

    signal = ai_engine.evaluate(signal)

    signal.decision = decision_engine.evaluate(signal)

    return signal