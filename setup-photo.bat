@echo off
REM Portfolio Photo Setup Script
REM This script creates the images folder and provides instructions

setlocal enabledelayedexpansion

set PORTFOLIO_DIR=%~dp0
set IMAGES_DIR=%PORTFOLIO_DIR%images

echo.
echo ========================================
echo Portfolio Photo Setup
echo ========================================
echo.

REM Create images folder if it doesn't exist
if not exist "%IMAGES_DIR%" (
    mkdir "%IMAGES_DIR%"
    echo [OK] Created 'images' folder
) else (
    echo [OK] 'images' folder already exists
)

echo.
echo ========================================
echo IMPORTANT: Next Steps
echo ========================================
echo.
echo 1. Open File Explorer
echo 2. Navigate to: %IMAGES_DIR%
echo 3. Copy your profile photo (1.jpg) into this folder
echo 4. Rename it to: profile.jpg
echo 5. Open index.html in your browser
echo.
echo Full path where to copy your photo:
echo %IMAGES_DIR%\profile.jpg
echo.
echo ========================================
echo.
pause
