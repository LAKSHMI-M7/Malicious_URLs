# 🔒 Malicious URL Detector - AI Security Suite

A modern, professional, and high-performance web application designed to detect malicious URLs using Machine Learning. This tool analyzes links for phishing, malware, and defacement patterns in real-time.

![Aesthetic Dashboard](https://via.placeholder.com/800x400.png?text=Malicious+URL+Detector+Dashboard)

## 🚀 Overview

The **Malicious URL Detector** leverages a **Random Forest Classifier** trained on over 650,000 URLs to categorize links into four distinct security levels. It features a sleek, cybersecurity-themed dashboard with glassmorphism aesthetics and real-time analysis reports.

### 🌟 Key Features
- **Real-time Prediction**: Instantly check if a URL is Benign, Phishing, Malware, or Defaced.
- **Cybersecurity UI**: Professional dark-themed dashboard with neon accents and fluid animations.
- **Detailed Insights**: View confidence scores and risk levels (Low, Medium, High).
- **Advanced ML**: Utilizes TF-IDF with character n-grams to detect subtle malicious patterns.
- **Responsive Design**: Fully optimized for both desktop and mobile devices.

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), Vanilla JavaScript, [Lucide Icons](https://lucide.dev/).
- **Backend**: Python 3.x, Flask.
- **Machine Learning**: Scikit-Learn (Random Forest), Pandas, NumPy, Joblib.
- **Vectorization**: TF-IDF (Character N-Grams range 3-5).

## 📁 Project Structure

```text
Malicious URLs/
├── app.py                # Main Flask Backend
├── train_model_v4.py     # ML Model Training Script (Char N-Grams)
├── static/
│   ├── css/style.css     # Premium UI Styling
│   └── js/script.js      # Frontend Logic & API Integration
├── templates/
│   └── index.html        # Main Application UI
├── malicious_phish.csv   # Dataset (650k+ URLs)
├── rf_model.joblib       # Saved Random Forest Model
├── tfidf_vectorizer.joblib # Saved TF-IDF Vectorizer
└── label_encoder.joblib  # Saved Label Mappings
```

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/malicious-url-detector.git
cd malicious-url-detector
```

### 2. Install Dependencies
```bash
pip install flask joblib scikit-learn pandas numpy
```

### 3. Training the Model (Optional)
If you wish to retrain the model with the latest dataset settings:
```bash
python train_model_v4.py
```

### 4. Run the Application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

## 🧠 Machine Learning Details

- **Algorithm**: Random Forest Classifier
- **Feature Extraction**: TF-IDF Vectorizer with `analyzer='char'` and `ngram_range=(3, 5)`. This ensures that substrings like `secure-login`, `hacked`, and `.php` are correctly identified regardless of their position.
- **Accuracy**: ~91%+ on the balanced testing set.
- **Labels**:
    - `0: Benign` (Safe)
    - `1: Defacement`
    - `2: Malware`
    - `3: Phishing`



---
*Disclaimer: This tool is for educational and showcase purposes. While highly accurate, always exercise caution when visiting unknown links.*
