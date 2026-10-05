$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "[1/5] Checking remote..."
git remote -v

Write-Host "[2/5] Fetching remote master..."
git fetch origin master

Write-Host "[3/5] Merging remote history..."
git merge origin/master --allow-unrelated-histories --no-edit

Write-Host "[4/5] Staging changes..."
git add -A
$staged = git diff --cached --name-only
if ($staged) {
    git commit -m "Sync local project with remote repository"
}

Write-Host "[5/5] Pushing master..."
git push -u origin master

Write-Host "SUCCESS: Repository synchronized and pushed." -ForegroundColor Green
