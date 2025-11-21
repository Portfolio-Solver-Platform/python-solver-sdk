from dataclasses import dataclass


@dataclass
class SolverConfig:
    class Queue:
        request_timeout: tuple[int, int] = (1, 5)

        class In:
            Name: str = os.getenv("QUEUE_IN_NAME")

        class Out:
            Name: str = os.getenv("QUEUE_OUT_NAME")

        class Auth:
            HOST: str = os.getenv(
                "RABBITMQ_HOST", "rabbitmq.rabbit-mq.svc.cluster.local"
            )
            PORT: str = int(os.getenv("RABBITMQ_PORT", "5672"))
            USER: str = os.getenv("RABBITMQ_USER", "guest")
            PASSWORD: str = os.getenv("RABBITMQ_PASSWORD", "guest")
