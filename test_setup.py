"""
Test script to verify the Leaf Disease Detection setup
"""
import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required packages are installed"""
    print("🔍 Testing package imports...")
    
    packages = {
        'streamlit': 'Streamlit',
        'fastapi': 'FastAPI',
        'groq': 'Groq',
        'uvicorn': 'Uvicorn',
        'requests': 'Requests',
        'dotenv': 'Python-dotenv'
    }
    
    failed = []
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"  ✅ {name} - OK")
        except ImportError:
            print(f"  ❌ {name} - FAILED")
            failed.append(name)
    
    return len(failed) == 0

def test_env_file():
    """Test if .env file exists and has API key"""
    print("\n🔍 Testing environment configuration...")
    
    env_path = Path('.env')
    if not env_path.exists():
        print("  ❌ .env file not found")
        return False
    
    print("  ✅ .env file exists")
    
    # Check if API key is configured
    with open(env_path, 'r') as f:
        content = f.read()
        if 'GROQ_API_KEY=' in content:
            if 'your_groq_api_key_here' in content:
                print("  ⚠️  GROQ_API_KEY not configured (still using placeholder)")
                print("     Please add your actual API key to .env file")
                return False
            else:
                print("  ✅ GROQ_API_KEY is configured")
                return True
    
    print("  ❌ GROQ_API_KEY not found in .env")
    return False

def test_project_structure():
    """Test if all required files exist"""
    print("\n🔍 Testing project structure...")
    
    required_files = [
        'main.py',
        'app.py',
        'requirements.txt',
        'utils.py',
        'Leaf Disease/main.py',
        'Leaf Disease/config.py'
    ]
    
    all_exist = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - NOT FOUND")
            all_exist = False
    
    return all_exist

def test_media_folder():
    """Test if Media folder has test images"""
    print("\n🔍 Testing Media folder...")
    
    media_path = Path('Media')
    if not media_path.exists():
        print("  ❌ Media folder not found")
        return False
    
    images = list(media_path.glob('*.jpg')) + list(media_path.glob('*.png'))
    if images:
        print(f"  ✅ Found {len(images)} test image(s)")
        for img in images:
            print(f"     - {img.name}")
        return True
    else:
        print("  ⚠️  No test images found in Media folder")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("  🌿 LEAF DISEASE DETECTION - SETUP VERIFICATION")
    print("=" * 60)
    print()
    
    results = {
        'Imports': test_imports(),
        'Environment': test_env_file(),
        'Project Structure': test_project_structure(),
        'Test Images': test_media_folder()
    }
    
    print("\n" + "=" * 60)
    print("  📊 TEST SUMMARY")
    print("=" * 60)
    
    for test, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"  {test}: {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("  🎉 ALL TESTS PASSED!")
        print("  You're ready to launch the application!")
        print("\n  Next steps:")
        print("  1. Ensure your Groq API key is in .env file")
        print("  2. Run: streamlit run main.py")
        print("     OR")
        print("     Run: uvicorn app:app --reload")
    else:
        print("  ⚠️  SOME TESTS FAILED")
        print("  Please fix the issues above before launching")
        
        if not results['Environment']:
            print("\n  🔑 To fix API key issue:")
            print("  1. Get your key from: https://console.groq.com/keys")
            print("  2. Open .env file")
            print("  3. Replace 'your_groq_api_key_here' with your actual key")
    
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
