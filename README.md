# 🔐 SafeLink Analyzer - Phishing URL Detection using AI & Machine Learning

SafeLink Analyzer is an AI-powered web-based tool designed to detect malicious and phishing URLs with high accuracy. This project combines machine learning models with an interactive Streamlit interface, allowing users to analyze links in real-time while offering features such as PDF report generation, screen sharing, voice and screen recording, and UI customization.

---

## 🚀 Features

- ✅ **Detect Fake or Real URLs** using a trained Machine Learning model.
- 🌐 **Streamlit Web App** for an intuitive and responsive frontend.
- 🧠 **AI-Driven Prediction** for accurate classification of URLs.
- 📄 **Save Results as PDF** to keep a record of predictions and analysis.
- 🔁 **Clear Cache** functionality for fresh sessions.
- 🎨 **Custom Themes & Text Color** options for accessibility and personalization.
- 🖥️ **Screen Sharing** for collaborative analysis or demos.
- 🎙️ **Record Voice & Screen** while interacting with the tool — useful for tutorials, walkthroughs, or training sessions.
- ☁️ **Free Deployment** on platforms like Streamlit Cloud.

---

## 🧠 How It Works

1. The user inputs a URL (e.g., `https://example.com`).
2. Feature extraction is done from the URL (e.g., length, presence of special characters, domain age).
3. The extracted features are passed into a Machine Learning model (e.g., Random Forest, SVM).
4. The model predicts whether the URL is **legitimate** or **malicious**.
5. Users can interact with the prediction results and export them as a **PDF report**.

---

## 📦 Tech Stack

| Layer       | Technologies |
|-------------|--------------|
| 🧠 AI/ML     | Scikit-learn, Pandas, NumPy |
| 🖥️ Frontend  | Streamlit |
| 📁 Backend   | Python |
| 📊 Model     | Trained ML Classifier (e.g., Random Forest) |
| 📃 Output    | PDF generation using `fpdf` / `reportlab` |
| 📺 Extras    | Screen recorder, voice capture (via browser extensions or Python wrappers) |

---

## 📷 Screenshots

| Prediction Page | PDF Report | Theme Customization | Screen Sharing |
|------------------|------------|----------------------| ----------------------|
| ![1](https://github.com/GunjalaSiddartha/SafeLink-Analyzer/blob/64e21b9aee55ed5cd50f3eab8800881c4a1308ca/output_detector.png) | ![2](https://github.com/GunjalaSiddartha/SafeLink-Analyzer/blob/64e21b9aee55ed5cd50f3eab8800881c4a1308ca/features_save_as_pdf.png) | ![3](https://github.com/GunjalaSiddartha/SafeLink-Analyzer/blob/64e21b9aee55ed5cd50f3eab8800881c4a1308ca/features_theme.png) | ![3](https://github.com/GunjalaSiddartha/SafeLink-Analyzer/blob/07671158c9b1b95d60b41d6d612d4c3f8a0a4797/ferures_shared_Screen.png) |


---

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/GunjalaSiddartha/SafeLink-Analyzer.git
cd SafeLink-Analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Main.py
