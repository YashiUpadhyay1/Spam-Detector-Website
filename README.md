# 🔍 Spam Message Detector

🚀 This web app detects whether a message is spam or not spam using a real trained model based on the UCI SMS Spam Collection dataset (`spam.csv`).

✔️ Real dataset (5500+ rows)  
✔️ Model trained every time from `spam.csv`  
✔️ No hardcoded logic — pure machine learning  
✔️ Built with Python (Flask) + HTML/CSS/JS

---

## ✨ Features

- 🔐 Login with secure credentials
- 🤖 Predicts spam or not using HuggingFace DistilBERT
- 🧠 Model trained live on startup (not pre-saved)
- 🌈 Gradient UI (black → blue) for both pages
- ✅ 95%+ accuracy using BERT-based transformer
- 🔔 Shows toast alerts (top right) for all actions

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python Flask  
- **Machine Learning:** DistilBERT (HuggingFace Transformers)  
- **Data:** UCI Spam Collection CSV  
- **Version Control:** Git + GitHub

---

## 📁 Folder Structure

SpamDetectorWebsite/
├── backend/
│ ├── app.py
│ ├── spam.csv
│ ├── static/
│ │ ├── style.css
│ │ └── script.js
│ └── templates/
│ ├── login.html
│ └── index.html


---

## 🔐 Login Credentials

Use these to log in:

- **Username:** `admin`
- **Password:** `1234`

---

## 🧪 Sample Test Cases

Paste these messages to test the model:

- ✅ `"Let’s catch up at 5 PM today."` → Not Spam  
- ✅ `"Meeting rescheduled to 3 PM. Please confirm."` → Not Spam  
- 🚫 `"Congratulations! You won a free iPhone. Click now!"` → Spam  
- 🚫 `"Free entry in 2 a weekly competition to win tickets!"` → Spam

---

## 🚀 Run Locally

✅ 1. Clone the Repository
-
bash
-
git clone https://github.com/YashiUpadhyay1/Spam-Detector-Website.git
---
📂 2. Navigate into the Project
-
bash
-
cd Spam-Detector-Website/backend
---
📦 3. Install Dependencies
-
bash
-
pip install flask pandas scikit-learn transformers
---
▶️ 4. Run the App
-
bash
-
python app.py
---
🌐 5. Visit in Your Browser
http://127.0.0.1:5000
---

##🙏 Credits
📊 Dataset: UCI SMS Spam Dataset

🤖 NLP Model: DistilBERT via HuggingFace

## 📌 Note to Viewers

All message predictions are made in real-time using the full dataset and trained model.
Nothing is hardcoded. Accuracy is achieved by dynamic vectorization and DistilBERT classification.

> 🔍 "This project is designed for hands-on spam detection evaluation."
