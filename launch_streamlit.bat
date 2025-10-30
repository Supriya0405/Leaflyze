@echo off
echo ========================================
echo        Leaflyze - Streamlit
echo   AI Leaf Disease Detection
echo ========================================
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.
echo Launching Streamlit application...
echo Access the app at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.
streamlit run main.py --server.port 8501
pause
