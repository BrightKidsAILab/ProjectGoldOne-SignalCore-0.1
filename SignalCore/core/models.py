from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Signal:

    pair: Optional[str] = None
    direction: Optional[str] = None

    entry: Optional[float] = None
    stop_loss: Optional[float] = None

    take_profits: List[float] = field(default_factory=list)

    confidence: int = 0

    risk_reward: Optional[float] = None

    source: str = ""

    received_at: datetime = field(default_factory=datetime.utcnow)

    valid: bool = False

    errors: List[str] = field(default_factory=list)