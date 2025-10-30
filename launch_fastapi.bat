@echo off
echo ========================================
echo        Leaflyze - FastAPI
echo   AI Leaf Disease Detection API
echo ========================================
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.
echo Launching FastAPI server...
echo API Documentation: http://localhost:8000/docs
echo Alternative Docs: http://localhost:8000/redoc
echo.
echo Press Ctrl+C to stop the server
echo.
uvicorn app:app --reload --host 0.0.0.0 --port 8000
pause
