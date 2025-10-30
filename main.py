
import streamlit as st
import requests

# Set Streamlit theme to wide mode with custom config
st.set_page_config(
    page_title="🌿 Leaflyze - AI Leaf Disease Detection",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🌿"
)

# Ultra-modern CSS with animations and glassmorphism
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2em 1em;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 2em;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        animation: fadeInDown 0.8s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .main-title {
        font-size: 3.5em;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        color: #2d3748;
        font-size: 1.3em;
        margin-top: 0.5em;
        font-weight: 400;
    }
    
    /* Upload section */
    .upload-section {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2em;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.5);
        animation: fadeInLeft 0.8s ease-out;
    }
    
    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Result card with glassmorphism */
    .result-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);
        padding: 2.5em;
        margin-top: 2em;
        border: 1px solid rgba(255, 255, 255, 0.5);
        animation: fadeInUp 0.8s ease-out;
        transition: all 0.3s ease;
    }
    
    .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Disease title with gradient */
    .disease-title {
        font-size: 2.8em;
        font-weight: 700;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5em;
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .healthy-title {
        font-size: 2.8em;
        font-weight: 700;
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5em;
    }
    
    /* Section titles */
    .section-title {
        color: #667eea;
        font-size: 1.5em;
        font-weight: 600;
        margin-top: 1.5em;
        margin-bottom: 0.8em;
        display: flex;
        align-items: center;
        gap: 0.5em;
    }
    
    .section-title::before {
        content: '';
        width: 4px;
        height: 24px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }
    
    /* Info badges with modern design */
    .info-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 0.6em 1.2em;
        font-size: 0.95em;
        font-weight: 600;
        margin-right: 0.8em;
        margin-bottom: 0.8em;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .info-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .severity-badge {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
    }
    
    .confidence-badge {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.4);
    }
    
    /* Lists with custom styling */
    .symptom-list, .cause-list, .treatment-list {
        list-style: none;
        padding-left: 0;
    }
    
    .symptom-list li, .cause-list li, .treatment-list li {
        padding: 0.8em 1.2em;
        margin-bottom: 0.8em;
        background: rgba(102, 126, 234, 0.1);
        border-left: 4px solid #667eea;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .symptom-list li:hover, .cause-list li:hover, .treatment-list li:hover {
        background: rgba(102, 126, 234, 0.2);
        transform: translateX(5px);
    }
    
    /* Timestamp */
    .timestamp {
        color: #718096;
        font-size: 0.95em;
        margin-top: 2em;
        text-align: right;
        font-style: italic;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.8em 2em;
        font-size: 1.1em;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6);
    }
    
    /* File uploader styling */
    .uploadedFile {
        border-radius: 15px;
        border: 2px dashed #667eea;
    }
    
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.9);
        padding: 2em;
        border-radius: 20px;
        border: 3px dashed #667eea;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #764ba2;
        background: rgba(255, 255, 255, 1);
        transform: scale(1.02);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Image styling */
    [data-testid="stImage"] {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }
    
    [data-testid="stImage"]:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.25);
    }
    
    /* Success/Error messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 15px;
        padding: 1.5em;
        backdrop-filter: blur(10px);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Add floating particles effect */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    /* Glow effect */
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.5); }
        50% { box-shadow: 0 0 40px rgba(102, 126, 234, 0.8); }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5em;
        }
        .subtitle {
            font-size: 1.1em;
        }
        .disease-title, .healthy-title {
            font-size: 2em;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Modern header with animation
st.markdown("""
    <div class='main-header'>
        <div style='font-size: 4em; margin-bottom: 0.2em;'>🌿</div>
        <h1 class='main-title'>Leaflyze</h1>
        <p class='subtitle'>🔬 AI-Powered Leaf Disease Detection • Instant Analysis • Expert Recommendations</p>
    </div>
""", unsafe_allow_html=True)

api_url = "http://localhost:8000"

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Centered upload section with enhanced styling
st.markdown("""
    <div style='text-align: center; margin-bottom: 2em;'>
        <div style='display: inline-block; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); 
                    padding: 3em 4em; border-radius: 30px; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
                    border: 1px solid rgba(255, 255, 255, 0.5); animation: fadeInUp 0.8s ease-out;'>
            <div style='font-size: 4em; margin-bottom: 0.3em;'>📤</div>
            <h2 style='color: #667eea; font-weight: 600; margin-bottom: 0.5em;'>Upload Your Leaf Image</h2>
            <p style='color: #718096; font-size: 1.1em;'>Drag & drop or click to browse</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Center the file uploader
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    uploaded_file = st.file_uploader(
        "Choose a leaf image", 
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

# Display preview and button in centered layout
if uploaded_file is not None:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create centered columns for image preview
    col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
    with col_img2:
        st.markdown("""
            <div style='text-align: center; background: rgba(255, 255, 255, 0.95); 
                        padding: 2em; border-radius: 25px; box-shadow: 0 15px 50px rgba(0, 0, 0, 0.15);
                        border: 1px solid rgba(255, 255, 255, 0.5); margin-bottom: 2em;'>
                <h3 style='color: #667eea; margin-bottom: 1em;'>📸 Image Preview</h3>
            </div>
        """, unsafe_allow_html=True)
        st.image(uploaded_file, use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🔍 Analyze & Detect Disease", use_container_width=True, type="primary"):
            with st.spinner("🔬 AI is analyzing your image..."):
                try:
                    files = {
                        "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post(
                        f"{api_url}/disease-detection-file", files=files)
                    if response.status_code == 200:
                        result = response.json()

                        # Display results in centered layout
                        col_res1, col_res2, col_res3 = st.columns([0.5, 3, 0.5])
                        with col_res2:
                            # Check if it's an invalid image
                            if result.get("disease_type") == "invalid_image":
                                st.markdown("<div class='result-card'>",
                                            unsafe_allow_html=True)
                                st.markdown(
                                    "<div class='disease-title' style='background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>⚠️ Invalid Image</div>", unsafe_allow_html=True)
                                st.markdown(
                                    "<div style='color: #ff5722; font-size: 1.2em; margin-bottom: 1.5em; font-weight: 500;'>❌ Please upload a clear image of a plant leaf for accurate disease detection.</div>", unsafe_allow_html=True)

                                # Show the symptoms (which contain the error message)
                                if result.get("symptoms"):
                                    st.markdown(
                                        "<div class='section-title'>❗ Issue Details</div>", unsafe_allow_html=True)
                                    st.markdown("<ul class='symptom-list'>",
                                                unsafe_allow_html=True)
                                    for symptom in result.get("symptoms", []):
                                        st.markdown(
                                            f"<li>• {symptom}</li>", unsafe_allow_html=True)
                                    st.markdown("</ul>", unsafe_allow_html=True)

                                # Show treatment recommendations
                                if result.get("treatment"):
                                    st.markdown(
                                        "<div class='section-title'>💡 What to Do</div>", unsafe_allow_html=True)
                                    st.markdown("<ul class='treatment-list'>",
                                                unsafe_allow_html=True)
                                    for treat in result.get("treatment", []):
                                        st.markdown(
                                            f"<li>✓ {treat}</li>", unsafe_allow_html=True)
                                    st.markdown("</ul>", unsafe_allow_html=True)

                                st.markdown("</div>", unsafe_allow_html=True)

                            elif result.get("disease_detected"):
                                st.markdown("<div class='result-card'>",
                                            unsafe_allow_html=True)
                                st.markdown(
                                    f"<div class='disease-title'>🦠 {result.get('disease_name', 'N/A')}</div>", unsafe_allow_html=True)
                                st.markdown(
                                    f"<span class='info-badge'>📋 Type: {result.get('disease_type', 'N/A').title()}</span>", unsafe_allow_html=True)
                                st.markdown(
                                    f"<span class='info-badge severity-badge'>⚠️ Severity: {result.get('severity', 'N/A').title()}</span>", unsafe_allow_html=True)
                                st.markdown(
                                    f"<span class='info-badge confidence-badge'>🎯 Confidence: {result.get('confidence', 'N/A')}%</span>", unsafe_allow_html=True)
                                st.markdown(
                                    "<div class='section-title'>🔍 Symptoms Detected</div>", unsafe_allow_html=True)
                                st.markdown("<ul class='symptom-list'>",
                                            unsafe_allow_html=True)
                                for symptom in result.get("symptoms", []):
                                    st.markdown(
                                        f"<li>• {symptom}</li>", unsafe_allow_html=True)
                                st.markdown("</ul>", unsafe_allow_html=True)
                                st.markdown(
                                    "<div class='section-title'>🌍 Possible Causes</div>", unsafe_allow_html=True)
                                st.markdown("<ul class='cause-list'>",
                                            unsafe_allow_html=True)
                                for cause in result.get("possible_causes", []):
                                    st.markdown(
                                        f"<li>• {cause}</li>", unsafe_allow_html=True)
                                st.markdown("</ul>", unsafe_allow_html=True)
                                st.markdown(
                                    "<div class='section-title'>💊 Recommended Treatment</div>", unsafe_allow_html=True)
                                st.markdown("<ul class='treatment-list'>",
                                            unsafe_allow_html=True)
                                for treat in result.get("treatment", []):
                                    st.markdown(
                                        f"<li>✓ {treat}</li>", unsafe_allow_html=True)
                                st.markdown("</ul>", unsafe_allow_html=True)
                                st.markdown(
                                    f"<div class='timestamp'>🕒 Analysis completed at {result.get('analysis_timestamp', 'N/A')}</div>", unsafe_allow_html=True)
                                st.markdown("</div>", unsafe_allow_html=True)
                            else:
                                # Healthy leaf case
                                st.markdown("<div class='result-card'>",
                                            unsafe_allow_html=True)
                                st.markdown(
                                    "<div class='healthy-title'>✅ Healthy Leaf Detected!</div>", unsafe_allow_html=True)
                                st.markdown(
                                    "<div style='color: #11998e; font-size: 1.3em; margin-bottom: 1.5em; font-weight: 500;'>🎉 Great news! No disease detected in this leaf. The plant appears to be in excellent health!</div>", unsafe_allow_html=True)
                                st.markdown(
                                    f"<span class='info-badge'>✨ Status: {result.get('disease_type', 'Healthy').title()}</span>", unsafe_allow_html=True)
                                st.markdown(
                                    f"<span class='info-badge confidence-badge'>🎯 Confidence: {result.get('confidence', 'N/A')}%</span>", unsafe_allow_html=True)
                                st.markdown(
                                    f"<div class='timestamp'>🕒 Analysis completed at {result.get('analysis_timestamp', 'N/A')}</div>", unsafe_allow_html=True)
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"API Error: {response.status_code}")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
