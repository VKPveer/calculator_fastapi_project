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

## GitHub push note
This repository is configured with:

`origin = https://github.com/VKPveer/calculator_fastapi_project.git`

If GitHub already contains an initial commit, a direct `git push origin master` can be rejected as a non-fast-forward update. Run one of the included sync scripts first:

Windows CMD:
`git_sync_and_push.bat`

PowerShell:
`powershell -ExecutionPolicy Bypass -File .\git_sync_and_push.ps1`

The script fetches the existing remote `master`, merges it safely (including unrelated initial histories), and then pushes the project.
