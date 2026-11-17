# PowerShell Script to Push AITR Lab 02 to GitHub
$RepoDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$GitExe = Join-Path (Split-Path -Parent $RepoDir) "mingit\cmd\git.exe"

if (-not (Test-Path $GitExe)) {
    $GitExe = "git"
}

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "AITR Lab 02: Pushing to GitHub Repository:" -ForegroundColor Cyan
Write-Host "https://github.com/sandeep-patidar-mns/Awesome-Context-Window-Degradation-and-Its-Impact-on-Long-Document-Research-Synthesis" -ForegroundColor Yellow
Write-Host "======================================================================" -ForegroundColor Cyan

Set-Location $RepoDir

Write-Host "`nLocal commits to be pushed:" -ForegroundColor Green
& $GitExe log --oneline -n 8

Write-Host "`nSelect an option to push:" -ForegroundColor Yellow
Write-Host "  [1] Standard Push (git push -u origin main)"
Write-Host "  [2] Pull and Rebase remote commits first (git pull --rebase origin main, then push)"
Write-Host "  [3] Overwrite / Force Push (git push -u origin main --force)"
$choice = Read-Host "Enter choice (1, 2, or 3) [Default: 1]"

if ($choice -eq "2") {
    Write-Host "`n[*] Pulling and rebasing from origin/main..." -ForegroundColor Cyan
    & $GitExe pull --rebase origin main
    Write-Host "`n[*] Pushing to origin/main..." -ForegroundColor Cyan
    & $GitExe push -u origin main
} elseif ($choice -eq "3") {
    Write-Host "`n[*] Force pushing complete project tree to origin/main..." -ForegroundColor Cyan
    & $GitExe push -u origin main --force
} else {
    Write-Host "`n[*] Executing standard push to origin/main..." -ForegroundColor Cyan
    & $GitExe push -u origin main
}

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n[SUCCESS] All files and commits have been pushed to GitHub!" -ForegroundColor Green
} else {
    Write-Host "`n[NOTICE] Push did not complete cleanly." -ForegroundColor Yellow
    Write-Host "If prompted for credentials, use your GitHub username and Personal Access Token (classic with repo scope)." -ForegroundColor White
}
