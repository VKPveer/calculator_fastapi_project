# Calculator FastAPI Project

A FastAPI calculator project designed for CoZo manifest-generation,
source synchronization, traceability, validation, and GitHub push testing.

## Version

Current test version: **1.3.0**

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
