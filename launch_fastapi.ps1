# Leaf Disease Detection - FastAPI Launcher
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  🔧 Leaf Disease Detection - FastAPI" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "Launching FastAPI server..." -ForegroundColor Yellow
Write-Host "API Documentation: " -NoNewline
Write-Host "http://localhost:8000/docs" -ForegroundColor Green
Write-Host "Alternative Docs: " -NoNewline
Write-Host "http://localhost:8000/redoc" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

# Launch FastAPI
uvicorn app:app --reload --host 0.0.0.0 --port 8000
