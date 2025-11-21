from .config import SolverConfig
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class SolverApi:
    config: SolverConfig
