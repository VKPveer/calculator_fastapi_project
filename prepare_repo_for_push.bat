@echo off
setlocal
cd /d "%~dp0"

echo ==============================================
echo Calculator FastAPI V3 - One-time Git Sync
echo ==============================================

git remote get-url origin >nul 2>&1
if errorlevel 1 (
  git remote add origin https://github.com/VKPveer/calculator_fastapi_project.git
)

git checkout master >nul 2>&1
if errorlevel 1 git checkout -b master

echo Fetching remote master...
git fetch origin master
if errorlevel 1 goto :fetch_failed

git merge-base --is-ancestor origin/master HEAD >nul 2>&1
if not errorlevel 1 goto :push

echo Remote history is not in local history. Merging...
git merge origin/master --allow-unrelated-histories -X ours --no-edit
if errorlevel 1 goto :merge_failed

:push
echo Pushing synchronized V3 repository...
git push origin master
if errorlevel 1 goto :push_failed

echo SUCCESS: V3 repository is synchronized.
exit /b 0

:fetch_failed
echo ERROR: Could not fetch origin/master.
exit /b 1

:merge_failed
echo ERROR: Automatic merge failed. Run git status.
exit /b 1

:push_failed
echo ERROR: Push failed. Check GitHub authentication/permissions.
exit /b 1
