# Leaf Disease Detection - Streamlit Launcher
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  🌿 Leaf Disease Detection - Streamlit" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "Launching Streamlit application..." -ForegroundColor Yellow
Write-Host "Access the app at: " -NoNewline
Write-Host "http://localhost:8501" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

# Launch Streamlit
streamlit run main.py --server.port 8501
