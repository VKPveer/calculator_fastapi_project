# CoZo V4 Selective-Change Verification Map

V4 is designed to verify that CoZo syncs only changed/new files rather than
rewriting the whole repository.

## Exactly one new source file

- `app/services/conversion_service.py`
  - class `ConversionService`
  - `celsius_to_fahrenheit`
  - `fahrenheit_to_celsius`
  - `kilometers_to_miles`

## Existing files intentionally changed

- `app/config.py`
- `app/__init__.py`
- `app/main.py`
- `tests/test_main.py`
- `README.md`
- `CHANGELOG.md`
- `COZO_TEST_VERIFICATION.md`

## Existing files intentionally NOT changed

- `app/models.py`
- `app/utils.py`
- `app/services/__init__.py`
- `app/services/calculator_service.py`
- `app/services/statistics_service.py`
- `app/services/finance_service.py`
- `tests/test_services.py`
- `requirements.txt`
- `.gitignore`
- `docs/ARCHITECTURE.md`
- Git helper scripts

## New API endpoints expected in app/main.py

- `POST /celsius-to-fahrenheit`
- `POST /fahrenheit-to-celsius`
- `POST /kilometers-to-miles`

## Expected GitHub source changes after sync

The source-sync commit should show the changed files above plus the newly
generated `project-manifest.json`. Unchanged files should retain their previous
Git commit timestamp/history.
