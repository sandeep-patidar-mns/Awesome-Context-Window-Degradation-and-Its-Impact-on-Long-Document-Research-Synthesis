@echo off
title Push AITR Lab 02 to GitHub
echo ======================================================================
echo AITR Lab 02: Pushing to GitHub Repository:
echo https://github.com/sandeep-patidar-mns/Awesome-Context-Window-Degradation-and-Its-Impact-on-Long-Document-Research-Synthesis
echo ======================================================================
echo.
cd /d "%~dp0"
echo Checking git status...
"..\mingit\cmd\git.exe" status
echo.
echo Pushing commits to GitHub (main branch)...
"..\mingit\cmd\git.exe" push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Everything has been pushed to your GitHub repository!
) else (
    echo [NOTE] If prompted for credentials, GitHub requires:
    echo   Username: sandeep-patidar-mns
    echo   Password: [Your GitHub Personal Access Token or browser login]
)
echo.
pause
