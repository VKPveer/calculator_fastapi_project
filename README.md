# Calculator FastAPI Project

A small FastAPI calculator application used to test CoZo project-manifest
generation, code-structure discovery, dependency mapping, traceability,
manifest-driven changes, validation, and GitHub update flows.

## Version

Current test version: **1.1.0**

## Project structure

```text
app/
├── __init__.py
├── main.py
├── models.py
└── services/
    ├── __init__.py
    └── calculator_service.py

tests/
└── test_main.py
```

## API endpoints

- `GET /`
- `GET /health/details`
- `POST /add`
- `POST /subtract`
- `POST /multiply`
- `POST /divide`
- `POST /power`
- `POST /square`
- `POST /average`
- `POST /absolute-difference`
- `POST /sum-of-squares`
- `POST /percentage`

## Example percentage request

```json
{
  "value": 250,
  "percentage": 12
}
```

Expected result:

```json
{
  "operation": "percentage",
  "value": 250,
  "percentage": 12,
  "result": 30
}
```

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Run tests

```bash
python -m pytest tests
```

## CoZo manifest test purpose

This version intentionally contains:

- multiple Python source files,
- Pydantic request models,
- a reusable service class,
- static methods,
- internal module imports,
- FastAPI endpoints,
- test functions,
- nested folders.

That makes it useful for verifying that the generated `project-manifest.json`
correctly captures files, classes, functions, methods, symbols, dependencies,
Git metadata, and traceability.

## Version 1.2.0 test additions

New endpoints for CoZo manifest verification:

- `POST /clamp`
- `POST /percentage-change`
- `POST /mean`
- `POST /range`

New source files:

- `app/utils.py`
- `app/services/statistics_service.py`

These additions are intentionally spread across models, utility functions, services,
API routes, and tests so the generated manifest can demonstrate file discovery,
symbols, internal dependencies, and test coverage.

