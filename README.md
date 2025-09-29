****Malicious URL Detection using Machine Learning****
 **Project Overview**
The internet is full of links—some safe, some harmful. Clicking on a malicious link can lead to phishing attacks, malware downloads, or defacement of websites.
This project aims to build an intelligent system that detects whether a given URL is safe or malicious using Machine Learning (ML).
With a simple Streamlit web application, users can enter a URL and instantly get predictions on its safety.

**Features**
1.Detects if a URL is Benign, Defacement, Malware, or Phishing.
2.Built with Random Forest Classifier for robust accuracy.
3.User-friendly Streamlit interface.
4.Real-time prediction from just a single input URL.

**Tech Stack**
1.Programming Language: Python 🐍
2.Libraries: Scikit-learn, Pandas, NumPy, Streamlit, Joblib
3.ML Algorithm: Random Forest Classifier
4.Interface: Streamlit (Web App)
 Model Performance
Accuracy: ~90%
5.Metrics (Precision, Recall, F1-score): Balanced across classes (Benign, Defacement, Malware, Phishing).

 **How to Run the Project**
1️⃣ Clone this repository:
git clone https://github.com/your-username/malicious-url-detection.git
cd malicious-url-detection
2️⃣ Install dependencies:
pip install -r requirements.txt
3️⃣ Run the Streamlit App:
streamlit run app.py
4️⃣ Open in browser → http://localhost:8501
