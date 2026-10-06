class CalculatorService:
    """Reusable calculator business logic used by API endpoints."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b

    @staticmethod
    def square(value: float) -> float:
        return value ** 2

    @staticmethod
    def average(a: float, b: float) -> float:
        return (a + b) / 2

    @staticmethod
    def absolute_difference(a: float, b: float) -> float:
        return abs(a - b)

    @staticmethod
    def sum_of_squares(a: float, b: float) -> float:
        return (a ** 2) + (b ** 2)

    @staticmethod
    def percentage(value: float, percentage: float) -> float:
        return value * (percentage / 100)
