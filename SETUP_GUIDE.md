# 🚀 Leaflyze - Complete Setup Guide
## AI-Powered Leaf Disease Detection System

## ✅ Setup Status

### Completed Steps:
- ✅ Python 3.13.6 verified
- ✅ Virtual environment created (`venv/`)
- ✅ All dependencies installed successfully
- ✅ `.env` configuration file created

---

## 🔑 Next Step: Configure Your Groq API Key

### 1. Get Your Groq API Key
- Visit: https://console.groq.com/keys
- Sign up or log in to your Groq account
- Create a new API key
- Copy the API key

### 2. Add API Key to .env File
Open the `.env` file in the project root and replace `your_groq_api_key_here` with your actual API key:

```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

**Important:** Keep your API key secure and never commit it to version control!

---

## 🚀 Launch the Application

### Option A: Streamlit Web Interface (Recommended for Users)

**Activate virtual environment and run:**
```powershell
.\venv\Scripts\Activate.ps1
streamlit run main.py --server.port 8501 --server.address 0.0.0.0
```

**Access the app at:** http://localhost:8501

**Features:**
- 🖼️ Drag-and-drop image upload
- 🔍 Real-time disease analysis
- 📊 Professional result display
- 📱 Responsive design

---

### Option B: FastAPI Backend Service (Recommended for Developers)

**Activate virtual environment and run:**
```powershell
.\venv\Scripts\Activate.ps1
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Access the API at:**
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc
- Root Endpoint: http://localhost:8000/

**API Endpoints:**
- `POST /disease-detection-file` - Upload image for disease detection
- `GET /` - API information and status

---

### Option C: Run Both Services (Full Stack)

**Terminal 1 - FastAPI:**
```powershell
.\venv\Scripts\Activate.ps1
uvicorn app:app --reload --port 8000
```

**Terminal 2 - Streamlit:**
```powershell
.\venv\Scripts\Activate.ps1
streamlit run main.py --server.port 8501
```

---

## 📡 Quick Start Commands

### Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```

### Deactivate Virtual Environment
```powershell
deactivate
```

### Verify Installation
```powershell
.\venv\Scripts\python.exe -c "import streamlit, fastapi, groq; print('✅ All dependencies installed successfully!')"
```

---

## 🧪 Testing the Application

### Test with Streamlit Interface
1. Launch Streamlit: `streamlit run main.py`
2. Upload a test image from `Media/` directory
3. Click "🔍 Detect Disease"
4. View results

### Test with API (cURL)
```powershell
curl -X POST "http://localhost:8000/disease-detection-file" `
  -H "accept: application/json" `
  -H "Content-Type: multipart/form-data" `
  -F "file=@Media/brown-spot-4 (1).jpg"
```

### Test with Python
```python
import requests

# Test API endpoint
url = "http://localhost:8000/disease-detection-file"
files = {"file": open("Media/brown-spot-4 (1).jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

---

## 📁 Project Structure

```
leaf-diseases-detect/
├── venv/                    # Virtual environment (created)
├── .env                     # Environment variables (created)
├── .env.example            # Environment template
├── main.py                 # Streamlit web interface
├── app.py                  # FastAPI backend service
├── requirements.txt        # Python dependencies
├── Leaf Disease/           # Core detection engine
│   ├── main.py            # Detection logic
│   └── config.py          # Configuration
├── Media/                  # Test images
├── utils.py               # Utility functions
├── test_api.py            # API tests
└── README.md              # Documentation
```

---

## 🔧 Configuration Options

Edit `.env` file to customize:

```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional
MODEL_NAME=meta-llama/llama-4-scout-17b-16e-instruct
MODEL_TEMPERATURE=0.3
MAX_COMPLETION_TOKENS=1024
LOG_LEVEL=INFO
```

---

## 🐛 Troubleshooting

### Issue: "Module not found" error
**Solution:** Ensure virtual environment is activated
```powershell
.\venv\Scripts\Activate.ps1
```

### Issue: "GROQ_API_KEY not found"
**Solution:** Check `.env` file exists and contains valid API key
```powershell
Get-Content .env
```

### Issue: Port already in use
**Solution:** Change port number
```powershell
# For Streamlit
streamlit run main.py --server.port 8502

# For FastAPI
uvicorn app:app --port 8001
```

### Issue: Execution policy error (PowerShell)
**Solution:** Run as administrator:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📊 Performance Benchmarks

- **Average Response Time:** 2-4 seconds per image
- **Accuracy Rate:** 85-95% across disease categories
- **Supported Formats:** JPEG, PNG, WebP, BMP, TIFF
- **Maximum Image Size:** 10MB per upload
- **Concurrent Requests:** Optimized for multiple simultaneous analyses

---

## 🌐 Deployment Options

### Vercel (Recommended)
```bash
npm install -g vercel
vercel --prod
```

### Streamlit Cloud
1. Push to GitHub
2. Connect at https://share.streamlit.io/
3. Add secrets in dashboard

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 📚 Additional Resources

- **Groq Documentation:** https://console.groq.com/docs
- **Streamlit Docs:** https://docs.streamlit.io/
- **FastAPI Docs:** https://fastapi.tiangolo.com/
- **Project Repository:** https://github.com/shukur-alom/leaf-diseases-detect

---

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| Activate venv | `.\venv\Scripts\Activate.ps1` |
| Run Streamlit | `streamlit run main.py` |
| Run FastAPI | `uvicorn app:app --reload` |
| Install deps | `pip install -r requirements.txt` |
| Test API | `python test_api.py` |
| Deactivate venv | `deactivate` |

---

## ✨ Features

### Streamlit Interface
- 🎨 Modern, responsive UI
- 📤 Drag-and-drop upload
- ⚡ Real-time analysis
- 📊 Detailed results display
- 🌿 Disease information & treatment

### FastAPI Backend
- 🚀 High-performance API
- 📝 Auto-generated documentation
- 🔒 Secure file handling
- 📊 Structured JSON responses
- 🧪 Easy testing with Swagger UI

### AI Detection Engine
- 🤖 Powered by Groq AI
- 🎯 High accuracy detection
- 📋 Comprehensive analysis
- 💊 Treatment recommendations
- 🔬 Multiple disease support

---

## 🆘 Support

If you encounter any issues:
1. Check this guide's troubleshooting section
2. Review the main README.md
3. Check GitHub issues
4. Ensure all dependencies are installed
5. Verify API key is correctly configured

---

**🎉 You're all set! Just add your Groq API key to `.env` and launch the application!**
