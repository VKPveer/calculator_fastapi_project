# CoZo Test Verification Map

After generating a manifest from this source folder, verify that it contains:

1. `app/main.py`
   - functions: `root`, `health_details`, `add`, `subtract`, `multiply`,
     `divide`, `power`, `square`, `average`, `absolute_difference`,
     `sum_of_squares`, `percentage`

2. `app/models.py`
   - classes: `CalculationRequest`, `SingleNumberRequest`, `PercentageRequest`

3. `app/services/calculator_service.py`
   - class: `CalculatorService`
   - methods: `add`, `subtract`, `multiply`, `divide`, `power`, `square`,
     `average`, `absolute_difference`, `sum_of_squares`, `percentage`

4. `tests/test_main.py`
   - 9 test functions

5. Internal dependencies
   - `app.main` -> `app.models`
   - `app.main` -> `app.services.calculator_service`

6. Documentation/support changes
   - `README.md`
   - `CHANGELOG.md`
   - `.gitignore`

## Version 1.2.0 verification

Verify the generated manifest also contains:

- `app/utils.py`
  - `clamp`
  - `percentage_change`
- `app/services/statistics_service.py`
  - class `StatisticsService`
  - methods `mean`, `range_value`
- `app/models.py`
  - `ClampRequest`
  - `PercentageChangeRequest`
  - `ValuesRequest`
- `app/main.py`
  - `clamp_value`
  - `calculate_percentage_change`
  - `mean`
  - `range_value`
- `tests/test_main.py`
  - `test_clamp`
  - `test_percentage_change`
  - `test_mean`
  - `test_range`

