# Calculator FastAPI Project

Simple calculator API built with FastAPI.

## Endpoints
- `GET /`
- `POST /add`
- `POST /subtract`
- `POST /multiply`
- `POST /divide`

Request body example:

```json
{
  "a": 10,
  "b": 5
}
```

## Run locally

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open Swagger UI at `http://127.0.0.1:8000/docs`.

## Tests

```bash
pytest
```
