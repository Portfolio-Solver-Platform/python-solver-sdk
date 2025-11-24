from typing import Callable
from .core import SolverApi
from .config import SolverConfig
import logging

# Prevent "No handlers found" warnings
logging.getLogger(__name__).addHandler(logging.NullHandler())


# It returns a FastAPI app, but I only type hint a Callable because I
# don't want it to be a part of the spec that it's a FastAPI app.
def psp_solver(solve: Callable, config: SolverConfig = SolverConfig()) -> Callable:
    pass
