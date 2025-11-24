import logging
from config import SolverConfig

logger = logging.getLogger(__name__)

config = SolverConfig()


class SolverWrapper:
    config: SolverConfig

    def __init__(self, config: SolverConfig):
        self.config = config
