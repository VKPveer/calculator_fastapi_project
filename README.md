# Calculator FastAPI Project

A FastAPI calculator project designed for CoZo manifest-generation,
source synchronization, traceability, validation, and GitHub push testing.

## Version

Current test version: **1.5.0**

## V3 purpose

V3 intentionally changes every tracked source/support file and adds new files so
you can verify the full flow:

```text
local source
→ /generate-manifest
→ /client/prepare-and-push-project
→ GitHub
```

## V3 project structure

```text
app/
├── __init__.py
├── config.py
├── main.py
├── models.py
├── utils.py
└── services/
    ├── __init__.py
    ├── calculator_service.py
    ├── finance_service.py
    └── statistics_service.py

docs/
└── ARCHITECTURE.md

tests/
├── test_main.py
└── test_services.py
```

## New V3 endpoints

- `POST /median`
- `POST /weighted-average`
- `POST /normalize`
- `POST /ratio`
- `POST /compound-amount`

Existing endpoints remain available.

## Generate manifest

Use the local V3 folder with `/generate-manifest`.

## Run tests

```bash
python -m pytest tests
```

## Verification

See `COZO_TEST_VERIFICATION.md` for the exact files, classes, methods, and
endpoints that should appear in the generated manifest and later on GitHub.


## V4 selective-change test

V4 intentionally changes only a subset of the V3 files and adds exactly one
new Python service file. This makes it easy to verify selective source sync.

### New V4 file

- `app/services/conversion_service.py`

### New V4 endpoints

- `POST /celsius-to-fahrenheit`
- `POST /fahrenheit-to-celsius`
- `POST /kilometers-to-miles`

Files such as `app/models.py`, `app/utils.py`,
`app/services/calculator_service.py`, `app/services/statistics_service.py`,
`app/services/finance_service.py`, and `tests/test_services.py` are intentionally
left unchanged from V3.


## V5 selective-change test

V5 intentionally changes only a small subset of V4 and adds exactly one new
service file so CoZo selective source synchronization can be verified.

### New V5 file

- `app/services/tax_service.py`

### New V5 endpoints

- `POST /tax-amount`
- `POST /total-with-tax`

### Existing files intentionally changed in V5

- `app/config.py`
- `app/__init__.py`
- `app/models.py`
- `app/main.py`
- `tests/test_main.py`
- `README.md`
- `CHANGELOG.md`
- `COZO_TEST_VERIFICATION.md`

All other V4 source/support files are intentionally left unchanged.
