class ConversionService:
    """Unit-conversion helpers added in V4 for CoZo sync testing."""

    KM_TO_MILES = 0.621371

    @staticmethod
    def celsius_to_fahrenheit(value: float) -> float:
        return (value * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(value: float) -> float:
        return (value - 32) * 5 / 9

    @classmethod
    def kilometers_to_miles(cls, value: float) -> float:
        return value * cls.KM_TO_MILES
