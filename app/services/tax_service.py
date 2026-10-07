class TaxService:
    """Small tax helpers added in V5 for selective-sync testing."""

    @staticmethod
    def tax_amount(amount: float, tax_percent: float) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        return amount * (tax_percent / 100)

    @staticmethod
    def total_with_tax(amount: float, tax_percent: float) -> float:
        return amount + TaxService.tax_amount(amount, tax_percent)
