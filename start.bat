@echo off
echo ====================================
echo   FastAPI Full Stack Project
echo ====================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        echo Make sure Python is installed and available in PATH
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import fastapi" 2>nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
    echo Dependencies installed successfully!
    echo.
)

REM Check if .env file exists
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file to set your configuration
    echo Press any key to open .env file in notepad...
    pause >nul
    notepad .env
    echo.
)

REM Start the FastAPI server
echo Starting FastAPI server...
echo.
echo Server will be available at:
echo   - Application: http://localhost:8000
echo   - API Docs: http://localhost:8000/docs
echo   - ReDoc: http://localhost:8000/redoc
echo.
echo Press Ctrl+C to stop the server
echo.

python main.py

REM If main.py fails, try uvicorn directly
if errorlevel 1 (
    echo.
    echo Trying alternative startup method...
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
)

echo.
echo Server stopped.
pause
