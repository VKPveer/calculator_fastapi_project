# CoZo V5 Selective-Change Verification Map

V5 verifies that CoZo synchronizes only selected changed files plus exactly
one new source file.

## Exactly one new source file

- `app/services/tax_service.py`
  - class `TaxService`
  - method `tax_amount`
  - method `total_with_tax`

## Existing files intentionally changed

- `app/config.py`
- `app/__init__.py`
- `app/models.py`
- `app/main.py`
- `tests/test_main.py`
- `README.md`
- `CHANGELOG.md`
- `COZO_TEST_VERIFICATION.md`

## Existing V4 files intentionally NOT changed

- `app/utils.py`
- `app/services/__init__.py`
- `app/services/calculator_service.py`
- `app/services/statistics_service.py`
- `app/services/finance_service.py`
- `app/services/conversion_service.py`
- `tests/test_services.py`
- `requirements.txt`
- `.gitignore`
- `docs/ARCHITECTURE.md`
- Git helper scripts

## New API endpoints expected in app/main.py

- `POST /tax-amount`
- `POST /total-with-tax`

## Expected GitHub source changes after sync

The commit should show the changed files above, the new
`app/services/tax_service.py`, and the regenerated `project-manifest.json`.
Unchanged V4 files should not appear in the source-change list.
