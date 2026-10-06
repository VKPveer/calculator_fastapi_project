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

## Automatic non-fast-forward fix

This package includes a Git `post-commit` hook at `.git/hooks/post-commit`.
When an external API commits changes and then runs `git push origin master`, the hook first fetches `origin/master`, incorporates remote history (including a GitHub-created initial README commit), and pushes the synchronized history. The API's following normal push should therefore succeed instead of returning a non-fast-forward / fetch-first error.

### One-time manual preparation (recommended after extracting)

Run either:

```bat
prepare_repo_for_push.bat
```

or:

```powershell
powershell -ExecutionPolicy Bypass -File .\prepare_repo_for_push.ps1
```

After that, your API can keep using a normal `git push origin master`.

## Manifest All-Files Integration Test
This line was added by `project-manifest.json` to verify README.md updates.
