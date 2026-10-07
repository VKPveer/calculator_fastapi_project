class FinanceService:
    """Finance-oriented calculation helpers."""

    @staticmethod
    def simple_interest(
        principal: float,
        annual_rate_percent: float,
        years: float,
    ) -> float:
        return principal * (annual_rate_percent / 100) * years

    @staticmethod
    def compound_amount(
        principal: float,
        annual_rate_percent: float,
        years: float,
        compounds_per_year: int = 1,
    ) -> float:
        rate = annual_rate_percent / 100
        return principal * (
            1 + rate / compounds_per_year
        ) ** (compounds_per_year * years)
