from statistics import median


class StatisticsService:
    """Statistics helpers for list-based calculator endpoints."""

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

    @staticmethod
    def median_value(values: list[float]) -> float:
        if not values:
            raise ValueError("values cannot be empty")
        return float(median(values))

    @staticmethod
    def weighted_average(
        values: list[float],
        weights: list[float],
    ) -> float:
        if len(values) != len(weights):
            raise ValueError("values and weights must have the same length")
        if not values:
            raise ValueError("values cannot be empty")

        total_weight = sum(weights)
        if total_weight == 0:
            raise ValueError("sum of weights cannot be zero")

        return sum(
            value * weight
            for value, weight in zip(values, weights)
        ) / total_weight
