# 🎯 NEXT STEPS - Leaflyze Setup
## You're Almost Ready!

## ✅ What's Already Done

- ✅ **Python 3.13.6** installed and verified
- ✅ **Virtual environment** created at `venv/`
- ✅ **All dependencies** installed successfully:
  - Streamlit (web interface)
  - FastAPI (API backend)
  - Groq (AI detection engine)
  - Uvicorn (server)
  - All other required packages
- ✅ **`.env` file** created from template
- ✅ **Project structure** verified
- ✅ **Test images** available in `Media/` folder

---

## 🔑 CRITICAL: Add Your Groq API Key (Required!)

### Step 1: Get Your Free Groq API Key

1. **Visit:** https://console.groq.com/keys
2. **Sign up** or **log in** to your Groq account (it's free!)
3. **Click** "Create API Key"
4. **Copy** the generated API key (starts with `gsk_`)

### Step 2: Add API Key to .env File

The `.env` file is currently open in your editor. You need to:

1. **Find this line:**
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

2. **Replace it with your actual key:**
   ```
   GROQ_API_KEY=gsk_your_actual_api_key_from_groq
   ```

3. **Save the file** (Ctrl+S)

**Example:**
```env
# Before (placeholder):
GROQ_API_KEY=your_groq_api_key_here

# After (with real key):
GROQ_API_KEY=gsk_abc123xyz789yourrealapikey
```

⚠️ **Important:** Keep your API key secure! Never share it or commit it to version control.

---

## 🚀 Launch the Application

Once you've added your API key, you have **3 easy ways** to launch:

### 🎨 Option 1: Streamlit Web Interface (Easiest!)

**Method A - Double-click the batch file:**
- Just double-click: `launch_streamlit.bat`

**Method B - Command line:**
```powershell
.\venv\Scripts\Activate.ps1
streamlit run main.py
```

**Access at:** http://localhost:8501

**Features:**
- Beautiful, user-friendly interface
- Drag-and-drop image upload
- Real-time disease detection
- Detailed results with treatment recommendations

---

### 🔧 Option 2: FastAPI Backend (For Developers)

**Method A - Double-click the batch file:**
- Just double-click: `launch_fastapi.bat`

**Method B - Command line:**
```powershell
.\venv\Scripts\Activate.ps1
uvicorn app:app --reload
```

**Access at:**
- API Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc
- Root: http://localhost:8000/

**Features:**
- RESTful API endpoints
- Interactive API documentation
- JSON responses
- Easy integration with other applications

---

### 🌐 Option 3: Run Both (Full Stack)

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

## 🧪 Test Your Setup

### Quick Verification Test
```powershell
.\venv\Scripts\python.exe test_setup.py
```

This will verify:
- ✅ All packages installed
- ✅ Environment configured
- ✅ Project structure correct
- ✅ Test images available

### Manual Test (After Launch)

**For Streamlit:**
1. Open http://localhost:8501
2. Upload `Media/brown-spot-4 (1).jpg`
3. Click "🔍 Detect Disease"
4. View the detailed analysis results

**For FastAPI:**
1. Open http://localhost:8000/docs
2. Click on `POST /disease-detection-file`
3. Click "Try it out"
4. Upload `Media/brown-spot-4 (1).jpg`
5. Click "Execute"
6. View JSON response

---

## 📋 Quick Command Reference

| Action | Command |
|--------|---------|
| **Activate venv** | `.\venv\Scripts\Activate.ps1` |
| **Run Streamlit** | `streamlit run main.py` |
| **Run FastAPI** | `uvicorn app:app --reload` |
| **Test Setup** | `python test_setup.py` |
| **Deactivate venv** | `deactivate` |
| **Check Python** | `python --version` |
| **View .env** | `Get-Content .env` |

---

## 🐛 Troubleshooting

### Issue: "GROQ_API_KEY not found"
**Solution:** 
- Open `.env` file
- Add your actual API key
- Save the file
- Restart the application

### Issue: "Module not found" error
**Solution:**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue: PowerShell execution policy error
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Port already in use
**Solution:**
```powershell
# For Streamlit - use different port
streamlit run main.py --server.port 8502

# For FastAPI - use different port
uvicorn app:app --port 8001
```

---

## 📊 What to Expect

### Performance
- **Response Time:** 2-4 seconds per image
- **Accuracy:** 85-95% across disease categories
- **Image Formats:** JPEG, PNG, WebP, BMP, TIFF
- **Max Size:** 10MB per upload

### Detection Capabilities
The AI can detect:
- ✅ Fungal diseases (e.g., Brown Spot, Leaf Rust)
- ✅ Bacterial diseases
- ✅ Viral diseases
- ✅ Nutrient deficiencies
- ✅ Pest damage
- ✅ Healthy leaves

### Output Information
For each detection, you'll get:
- 🦠 **Disease Name**
- 📊 **Confidence Level** (percentage)
- 🔬 **Disease Type** (fungal, bacterial, viral, etc.)
- ⚠️ **Severity Level** (mild, moderate, severe)
- 🔍 **Symptoms** (detailed list)
- 🌍 **Possible Causes** (environmental factors)
- 💊 **Treatment Recommendations** (actionable steps)
- 🕒 **Analysis Timestamp**

---

## 🎯 Your Checklist

- [ ] Get Groq API key from https://console.groq.com/keys
- [ ] Add API key to `.env` file (currently open in your editor)
- [ ] Save the `.env` file
- [ ] Run `test_setup.py` to verify everything
- [ ] Launch the application (Streamlit or FastAPI)
- [ ] Test with sample image from `Media/` folder
- [ ] Enjoy detecting leaf diseases! 🌿

---

## 📚 Additional Resources

- **Full Setup Guide:** `SETUP_GUIDE.md`
- **Quick Reference:** `QUICK_START.txt`
- **Project README:** `README.md`
- **Groq Documentation:** https://console.groq.com/docs
- **Streamlit Docs:** https://docs.streamlit.io/
- **FastAPI Docs:** https://fastapi.tiangolo.com/

---

## 🆘 Need Help?

1. Check `SETUP_GUIDE.md` for detailed instructions
2. Run `test_setup.py` to diagnose issues
3. Review troubleshooting section above
4. Check GitHub issues: https://github.com/shukur-alom/leaf-diseases-detect/issues

---

## 🎉 Ready to Go!

Once you've added your API key to the `.env` file:

1. **Save the file** (Ctrl+S)
2. **Double-click** `launch_streamlit.bat` or `launch_fastapi.bat`
3. **Upload** a leaf image
4. **Get instant** disease detection results!

**You're all set! Happy detecting! 🌿🔍**
