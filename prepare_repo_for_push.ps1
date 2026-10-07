$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$origin = "https://github.com/VKPveer/calculator_fastapi_project.git"

Write-Host "Calculator FastAPI V3 - One-time Git Sync"

try { git remote get-url origin | Out-Null }
catch { git remote add origin $origin }

& git checkout master 2>$null
if ($LASTEXITCODE -ne 0) { & git checkout -b master }

Write-Host "Fetching origin/master..."
& git fetch origin master
if ($LASTEXITCODE -ne 0) { throw "Could not fetch origin/master." }

& git merge-base --is-ancestor origin/master HEAD
if ($LASTEXITCODE -ne 0) {
    Write-Host "Remote contains commits not present locally. Merging safely..."
    & git merge origin/master --allow-unrelated-histories -X ours --no-edit
    if ($LASTEXITCODE -ne 0) { throw "Automatic merge failed. Run git status." }
}

Write-Host "Pushing synchronized V3 master..."
& git push origin master
if ($LASTEXITCODE -ne 0) { throw "Push failed. Check GitHub authentication/permissions." }

Write-Host "SUCCESS: V3 repository is synchronized." -ForegroundColor Green
