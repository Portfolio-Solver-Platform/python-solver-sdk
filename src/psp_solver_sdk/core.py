from .config import SolverConfig
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class SolverWrapper:
    config: SolverConfig

    def __init__(config: SolverConfig):
        self.config = config
