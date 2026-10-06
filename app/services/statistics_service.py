class StatisticsService:
    """Small statistics helpers for calculator API examples."""

    @staticmethod
    def mean(values: list[float]) -> float:
        if not values:
            raise ValueError("values cannot be empty")
        return sum(values) / len(values)

    @staticmethod
    def range_value(values: list[float]) -> float:
        if not values:
            raise ValueError("values cannot be empty")
        return max(values) - min(values)
