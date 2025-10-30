🌿 Leaflyze: Smart Leaf Disease Detection System
🧠 Overview

Leaflyze is an AI-powered system designed to detect and classify plant leaf diseases with high accuracy.
It helps farmers and researchers identify crop issues early, enabling timely treatment and improved yield.

⚙️ Key Features

🖼️ Detects diseases from leaf images using a trained deep learning model (.h5).

🔍 Provides real-time prediction through a clean web interface (Streamlit or FastAPI).

☁️ Easily deployable to cloud services like AWS or Google Cloud.

📊 Generates confidence scores and possible disease types.

🧩 Tech Stack
Component	Technology Used
Language	Python
Framework	TensorFlow / Keras
Web Interface	Streamlit / FastAPI
Data Handling	NumPy, Pandas
Visualization	Matplotlib, OpenCV
Environment	Jupyter Notebook, VS Code
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Supriya0405/Leaflyze.git
cd Leaflyze

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py


OR, if you’re using FastAPI:

python -m uvicorn app:app --reload

4️⃣ Upload a Leaf Image 🌿

The model predicts the disease name and confidence percentage.

🧠 Model Training

The model (Leaf Deases(96,88).h5) is trained on a dataset containing various diseased and healthy leaf images.
The training uses CNN architecture for efficient feature extraction and classification.

📈 Future Enhancements

🌎 Cloud integration for mobile access

🤖 Improved model accuracy with GAN-based augmentation

📱 Android app interface

☁️ IoT integration for field sensors

👩‍💻 Developed by

Supriya Venkatasalapathi
Pre-final year B.Tech IT | AWS Cloud | Linux  | MERN Stack Developer | Open to Internships & Collaborations

📫 Connect:
LinkedIn
https://www.linkedin.com/in/supriya-v-026002287/

🪴 License

This project is open-source under the MIT License.
Feel free to modify and enhance for your own research or development work.
