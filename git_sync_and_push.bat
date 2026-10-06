@echo off
setlocal
cd /d "%~dp0"

echo [1/5] Checking remote...
git remote -v

echo [2/5] Fetching remote master...
git fetch origin master
if errorlevel 1 goto :error

echo [3/5] Merging remote history...
git merge origin/master --allow-unrelated-histories --no-edit
if errorlevel 1 (
  echo.
  echo Merge conflict detected. Resolve conflicts, then run this file again.
  exit /b 1
)

echo [4/5] Staging any resolved/project changes...
git add -A

git diff --cached --quiet
if errorlevel 1 git commit -m "Sync local project with remote repository"

echo [5/5] Pushing master...
git push -u origin master
if errorlevel 1 goto :error

echo.
echo SUCCESS: Repository synchronized and pushed.
exit /b 0

:error
echo.
echo ERROR: Git sync/push failed. See message above.
exit /b 1
REM MANIFEST_ALL_FILES_TEST: git_sync_and_push.bat updated by project-manifest.json
