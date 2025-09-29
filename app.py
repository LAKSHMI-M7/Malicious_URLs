# app.py
import streamlit as st
import joblib

# Load saved files (created by train_and_save.py)
model = joblib.load("rf_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")
encoder = joblib.load("label_encoder.joblib")

st.set_page_config(page_title="Malicious URL Detector", layout="centered")
st.title("🔒 Malicious URL Detector")

st.write("Enter a URL below and click **Check URL** to predict whether it's benign or malicious.")

user_url = st.text_input("Enter URL", "")

if st.button("Check URL"):
    if user_url.strip() == "":
        st.warning("Please enter a URL.")
    else:
        # Transform and predict
        user_feature = vectorizer.transform([user_url])
        pred = model.predict(user_feature)[0]
        label = encoder.inverse_transform([pred])[0]
        st.success(f"✅ Prediction: **{label}**")
        st.write(f"Model class index: {pred}")



