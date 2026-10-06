@echo off
setlocal
cd /d "%~dp0"

echo ==============================================
echo Calculator FastAPI - One-time Git Sync
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
echo Pushing synchronized repository...
git push origin master
if errorlevel 1 goto :push_failed

echo.
echo SUCCESS: Repository is synchronized. The /git/commit-push API can now use normal git push origin master.
exit /b 0

:fetch_failed
echo ERROR: Could not fetch origin/master. Check internet/GitHub access.
exit /b 1

:merge_failed
echo ERROR: Automatic merge failed. Run git status to inspect conflicts.
exit /b 1

:push_failed
echo ERROR: Push failed. Check GitHub authentication/permissions.
exit /b 1
REM MANIFEST_ALL_FILES_TEST: prepare_repo_for_push.bat updated by project-manifest.json
