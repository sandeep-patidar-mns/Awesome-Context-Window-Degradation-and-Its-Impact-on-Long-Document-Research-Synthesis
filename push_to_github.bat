@echo off
title Push AITR Lab 02 to GitHub
echo ======================================================================
echo AITR Lab 02: Push Complete Implementation to GitHub
echo Target Repository:
echo https://github.com/sandeep-patidar-mns/Awesome-Context-Window-Degradation-and-Its-Impact-on-Long-Document-Research-Synthesis
echo ======================================================================
echo.
cd /d "%~dp0"

echo [1/3] Checking Git Status and Local Commit History...
"..\mingit\cmd\git.exe" status -s
echo.
echo Local Commits ready to push:
"..\mingit\cmd\git.exe" log --oneline -n 8
echo.
echo ======================================================================
echo Choose how to upload your commits:
echo   [1] Standard Push (git push -u origin main)
echo   [2] Pull and Rebase existing remote commits first, then push
echo   [3] Force Push (git push -u origin main --force)
echo       *Use [3] if remote has older draft commits that you want to replace
echo        with this complete 18-prompt project tree.
echo ======================================================================
set /p choice="Enter choice (1, 2, or 3) [Default 1]: "

if "%choice%"=="2" goto opt_pull
if "%choice%"=="3" goto opt_force
goto opt_standard

:opt_standard
echo.
echo [*] Executing: git push -u origin main
"..\mingit\cmd\git.exe" push -u origin main
goto end_check

:opt_pull
echo.
echo [*] Executing: git pull --rebase origin main
"..\mingit\cmd\git.exe" pull --rebase origin main
echo [*] Executing: git push -u origin main
"..\mingit\cmd\git.exe" push -u origin main
goto end_check

:opt_force
echo.
echo [*] Executing: git push -u origin main --force
"..\mingit\cmd\git.exe" push -u origin main --force
goto end_check

:end_check
echo.
if %ERRORLEVEL% EQU 0 (
    echo ======================================================================
    echo [SUCCESS] All files and commits have been pushed to GitHub!
    echo Visit: https://github.com/sandeep-patidar-mns/Awesome-Context-Window-Degradation-and-Its-Impact-on-Long-Document-Research-Synthesis
    echo ======================================================================
) else (
    echo ======================================================================
    echo [NOTE / TROUBLESHOOTING]:
    echo 1. If Git prompted for credentials:
    echo    Username: sandeep-patidar-mns
    echo    Password: Use a GitHub Personal Access Token (classic with repo scope)
    echo 2. If rejected due to remote history, rerun and choose Option [3] (Force Push)
    echo    or Option [2] (Rebase).
    echo ======================================================================
)
echo.
pause
