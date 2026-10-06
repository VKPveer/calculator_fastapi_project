import pytest

from app.services import CalculatorService, FinanceService, StatisticsService
from app.utils import normalize


def test_calculator_ratio():
    assert CalculatorService.ratio(9, 3) == 3


def test_ratio_zero_denominator():
    with pytest.raises(ValueError):
        CalculatorService.ratio(10, 0)


def test_statistics_median():
    assert StatisticsService.median_value([1, 9, 3]) == 3


def test_weighted_average_validation():
    with pytest.raises(ValueError):
        StatisticsService.weighted_average([1, 2], [1])


def test_finance_compound_amount():
    result = FinanceService.compound_amount(1000, 10, 2, 1)
    assert round(result, 2) == 1210


def test_normalize():
    assert normalize(25, 0, 100) == 0.25
