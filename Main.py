# app.py

import streamlit as st
from API import get_prediction

# Title
st.title("🌐 SafeLink Analyzer - Phishing URL Detection using AI & Machine Learning")

# Description
st.markdown("""
Input a website URL below to evaluate its safety. The system will analyze and classify it as either **malicious** or **safe**.""")

# Input URL
url = st.text_input("Enter Website URL:")

# Path to trained model
model_path = "./models/Malicious_URL_Prediction.h5"

# Predict Button
if st.button("Predict"):
    if url:
        with st.spinner("Analyzing URL..."):
            prediction = get_prediction(url, model_path)

            # Display result
            if prediction >= 50:
                st.error(f"⚠️ Warning: This URL is {prediction}% likely to be malicious!")
            else:
                st.success(f"✅ Safe: This URL is only {prediction}% likely to be malicious.")
    else:
        st.warning("Please enter a URL to predict.")
