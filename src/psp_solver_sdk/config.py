from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class CpuConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CPU_")

    limit: int = Field(gt=0)


class QueueAuthConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="QUEUE_")

    host: str
    # Enforce valid port range (non-privileged ports)
    port: int = Field(ge=1024, le=65535)
    user: str
    password: str


class QueueConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="QUEUE_")

    request_timeout: tuple[int, int] = (1, 5)
    in_name: str
    out_name: str

    auth: QueueAuthConfig = Field(default_factory=QueueAuthConfig)


class SolverConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="")

    cpu: CpuConfig = Field(default_factory=CpuConfig)
    queue: QueueConfig = Field(default_factory=QueueConfig)
