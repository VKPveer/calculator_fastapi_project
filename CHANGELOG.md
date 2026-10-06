# Changelog

## 1.4.0 - Selective source-sync test

Changed only selected V3 files:
- `app/config.py`
- `app/__init__.py`
- `app/main.py`
- `tests/test_main.py`
- `README.md`
- `CHANGELOG.md`
- `COZO_TEST_VERIFICATION.md`

Added exactly one new source file:
- `app/services/conversion_service.py`

Added endpoints:
- `POST /celsius-to-fahrenheit`
- `POST /fahrenheit-to-celsius`
- `POST /kilometers-to-miles`

## 1.3.0 - Full repository change test

Changed:
- all existing Python source files
- test suite
- README and verification documentation
- Git helper scripts
- `.gitignore`
- `requirements.txt`

Added:
- `app/config.py`
- `app/services/finance_service.py`
- `tests/test_services.py`
- `docs/ARCHITECTURE.md`
- `/median`
- `/weighted-average`
- `/normalize`
- `/ratio`
- `/compound-amount`

## 1.2.0 - Expanded semantic-manifest test

Added utility and statistics functionality.

## 1.1.0 - Initial semantic-manifest expansion

Added models, service-layer calculator logic, and expanded API tests.
