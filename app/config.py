from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    name: str = "Calculator API"
    version: str = "1.3.0"
    description: str = (
        "Calculator API with calculator, statistics, finance, and utility services."
    )


CONFIG = AppConfig()
