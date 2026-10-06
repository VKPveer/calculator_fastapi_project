@echo off
setlocal
cd /d "%~dp0"

echo Calculator FastAPI V3 - Safe Git Sync
echo [1/5] Checking remote...
git remote -v

echo [2/5] Fetching remote master...
git fetch origin master
if errorlevel 1 goto :error

echo [3/5] Merging remote history...
git merge origin/master --allow-unrelated-histories --no-edit
if errorlevel 1 (
  echo Merge conflict detected. Resolve conflicts, then run this file again.
  exit /b 1
)

echo [4/5] Staging changes...
git add -A
git diff --cached --quiet
if errorlevel 1 git commit -m "Sync Calculator FastAPI V3 with remote repository"

echo [5/5] Pushing master...
git push -u origin master
if errorlevel 1 goto :error

echo SUCCESS: V3 repository synchronized and pushed.
exit /b 0

:error
echo ERROR: V3 Git sync/push failed. See message above.
exit /b 1
