import os
import joblib
import traceback
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'rf_model.joblib')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'tfidf_vectorizer.joblib')
ENCODER_PATH = os.path.join(BASE_DIR, 'label_encoder.joblib')

# Global variables
model = None
vectorizer = None
encoder = None

# Custom Tokenizer (Required if the vectorizer was trained with a custom tokenizer)
# For the new character-level model (v4), this might not be strictly used by the vectorizer object itself
# but we keep it to prevent any attribute errors if an older object is loaded or if referenced.
def make_tokens(f):
    # Split by slash, dot, hyphen
    tokens_by_slash = str(f).split('/')
    total_tokens = []
    for i in tokens_by_slash:
        # Split by dot
        tokens = str(i).split('.') 
        total_tokens += tokens
    return list(set(total_tokens))

def load_models():
    global model, vectorizer, encoder
    try:
        print(f"Loading models from {BASE_DIR}...")
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            print("Model loaded.")
        else:
            print("Model file not found!")
            
        if os.path.exists(VECTORIZER_PATH):
            # The vectorizer relies on make_tokens being available
            vectorizer = joblib.load(VECTORIZER_PATH)
            print("Vectorizer loaded.")
        else:
            print("Vectorizer file not found!")
            
        if os.path.exists(ENCODER_PATH):
            encoder = joblib.load(ENCODER_PATH)
            print("Encoder loaded.")
        else:
            print("Encoder file not found!")
            
    except Exception as e:
        print(f"Error loading models: {e}")
        traceback.print_exc()

load_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if not model or not vectorizer:
            return jsonify({'error': 'Model or Vectorizer not loaded properly on server.'}), 500
        
        data = request.json
        if not data or 'url' not in data:
            return jsonify({'error': 'No URL provided'}), 400
        
        user_url = data['url']
        
        # 1. Transform input
        user_feature = vectorizer.transform([user_url])
        
        # 2. Predict
        pred = model.predict(user_feature)[0]
        
        # 3. Decode label
        label_name = "Unknown"
        if encoder:
            try:
                # inverse_transform expects an array-like
                label_name = encoder.inverse_transform([pred])[0]
            except Exception as e:
                print(f"Encoder inverse_transform failed: {e}")
                mapping = {0: 'benign', 1: 'defacement', 2: 'malware', 3: 'phishing'}
                label_name = mapping.get(pred, 'unknown')
        else:
             mapping = {0: 'benign', 1: 'defacement', 2: 'malware', 3: 'phishing'}
             label_name = mapping.get(pred, 'unknown')
             
        # 4. Determine Risk Level & UI Display
        label_lower = str(label_name).lower()
        
        if 'benign' in label_lower:
            display_label = "Safe (Benign)"
            risk = "Low"
        elif 'defacement' in label_lower:
            display_label = "Defacement"
            risk = "Medium"
        elif 'phishing' in label_lower:
            display_label = "Phishing"
            risk = "High"
        elif 'malware' in label_lower:
            display_label = "Malware"
            risk = "High"
        else:
            display_label = label_name.capitalize()
            risk = "High"
            
        # 5. Confidence Score
        confidence = 0
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(user_feature)[0]
            confidence = round(max(probabilities) * 100, 2)
        
        return jsonify({
            'label': display_label,
            'risk': risk,
            'confidence': confidence
        })

    except Exception as e:
        print(f"Prediction Error: {e}")
        traceback.print_exc()
        return jsonify({'error': f"Internal Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
