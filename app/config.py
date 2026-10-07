from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    name: str = "Calculator API"
    version: str = "1.5.0"
    description: str = (
        "Calculator API with calculator, statistics, finance, utility, conversion, and tax services."
    )


CONFIG = AppConfig()
