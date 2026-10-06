# Changelog

## 1.1.0 - CoZo manifest-generation test expansion

Added:
- `app/models.py`
- `app/services/calculator_service.py`
- `app/services/__init__.py`
- `GET /health/details`
- `POST /average`
- `POST /absolute-difference`
- `POST /sum-of-squares`
- `POST /percentage`
- expanded automated tests
- service-layer separation for calculator operations

## 1.2.0 - Expanded semantic-manifest test

Added:
- `app/utils.py` with `clamp` and `percentage_change`
- `app/services/statistics_service.py` with `StatisticsService`
- `ClampRequest`, `PercentageChangeRequest`, `ValuesRequest`
- `/clamp`, `/percentage-change`, `/mean`, `/range`
- four additional API tests

