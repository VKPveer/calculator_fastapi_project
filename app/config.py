from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    name: str = "Calculator API"
    version: str = "1.4.0"
    description: str = (
        "Calculator API with calculator, statistics, finance, utility, and conversion services."
    )


CONFIG = AppConfig()
