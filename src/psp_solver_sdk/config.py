from dataclasses import dataclass


@dataclass
class SolverConfig:
    class CPU:
        limit: int = os.getenv("CPU_LIMIT")

    class Queue:
        request_timeout: tuple[int, int] = (1, 5)

        class In:
            name: str = os.getenv("QUEUE_IN_NAME")

        class Out:
            name: str = os.getenv("QUEUE_OUT_NAME")

        class Auth:
            host: str = os.getenv("QUEUE_HOST")
            port: int = int(os.getenv("QUEUE_PORT"))
            user: str = os.getenv("QUEUE_USER")
            password: str = os.getenv("QUEUE_PASSWORD")
