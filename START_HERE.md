# 🚀 START HERE - Leaflyze Quick Launch Guide

## When You Open This Folder Again

You only need **2 simple steps** to launch the application:

---

## 🎨 Method 1: Streamlit Web Interface (Easiest!)

### Option A: Double-Click (Simplest!)
Just **double-click** this file:
```
launch_streamlit.bat
```
That's it! The app will start automatically.

### Option B: PowerShell Commands
Open PowerShell in this folder and run:
```powershell
.\venv\Scripts\Activate.ps1
streamlit run main.py
```

**Access at:** http://localhost:8501

---

## 🔧 Method 2: FastAPI Backend

### Option A: Double-Click
Just **double-click** this file:
```
launch_fastapi.bat
```

### Option B: PowerShell Commands
Open PowerShell in this folder and run:
```powershell
.\venv\Scripts\Activate.ps1
uvicorn app:app --reload
```

**Access at:** http://localhost:8000/docs

---

## 📋 That's All You Need!

**No need to:**
- ❌ Reinstall Python
- ❌ Recreate virtual environment
- ❌ Reinstall dependencies
- ❌ Reconfigure .env file

**Everything is already set up!** Just activate the virtual environment and run the app.

---

## 🎯 Quick Reference

### To Start the App:
1. **Open PowerShell** in this folder (or double-click `.bat` file)
2. **Activate venv:** `.\venv\Scripts\Activate.ps1`
3. **Run app:** `streamlit run main.py`

### To Stop the App:
- Press **Ctrl+C** in the terminal

### To Restart:
- Just run the commands again (no need to deactivate)

---

## 🆘 If Something Goes Wrong

### Virtual environment not found?
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### API key error?
- Check that `.env` file still has your Groq API key
- Open `.env` and verify: `GROQ_API_KEY=gsk_your_key_here`

### Port already in use?
```powershell
# Use different port
streamlit run main.py --server.port 8502
```

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| **launch_streamlit.bat** | Double-click to start Streamlit |
| **launch_fastapi.bat** | Double-click to start FastAPI |
| **START_HERE.md** | This file - quick start guide |
| **NEXT_STEPS.md** | Detailed instructions |
| **.env** | Your API key (keep secure!) |

---

## 💡 Pro Tips

### Fastest Way to Launch:
1. Navigate to folder in File Explorer
2. Double-click `launch_streamlit.bat`
3. Wait for browser to open
4. Upload leaf image and detect!

### Using PowerShell:
```powershell
# Navigate to folder
cd C:\Users\SUPRIYA\Desktop\leaf-diseases-detect

# Launch Streamlit
.\venv\Scripts\Activate.ps1
streamlit run main.py

# Or launch FastAPI
.\venv\Scripts\Activate.ps1
uvicorn app:app --reload
```

### Check if Everything Still Works:
```powershell
.\venv\Scripts\python.exe test_setup.py
```

---

## 🎉 Summary

**Every time you open this folder:**

1. **Double-click** `launch_streamlit.bat`
   
   **OR**

2. Open PowerShell and run:
   ```powershell
   .\venv\Scripts\Activate.ps1
   streamlit run main.py
   ```

**That's it! No reinstallation needed!** 🌿✨
