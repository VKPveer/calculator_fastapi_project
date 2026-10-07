# CoZo V3 Test Verification Map

After `/generate-manifest`, verify the manifest contains all of these.

## New files

- `app/config.py`
- `app/services/finance_service.py`
- `tests/test_services.py`
- `docs/ARCHITECTURE.md`

## Updated source symbols

### app/config.py
- `AppConfig`
- `CONFIG`

### app/models.py
- `CalculationRequest`
- `ClampRequest`
- `PercentageChangeRequest`
- `PercentageRequest`
- `ValuesRequest`
- `WeightedAverageRequest`
- `CompoundInterestRequest`
- `NormalizeRequest`

### app/services/calculator_service.py
- `CalculatorService.midpoint`
- `CalculatorService.ratio`

### app/services/statistics_service.py
- `StatisticsService.median_value`
- `StatisticsService.weighted_average`

### app/services/finance_service.py
- `FinanceService.simple_interest`
- `FinanceService.compound_amount`

### app/utils.py
- `normalize`
- `round_result`

### app/main.py
- `median_value`
- `weighted_average`
- `normalize_value`
- `ratio`
- `compound_amount`

## New tests

`tests/test_services.py` should contain service-level tests.

## GitHub verification after client sync

The GitHub commit should show changes to every tracked source/support file plus
the newly generated `project-manifest.json`.
