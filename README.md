# 🗳️ Political Bias Detector using BERT

This project uses a fine-tuned BERT model to detect political bias (Left, Center, Right) in news articles. It allows users to input text or provide a URL (via web scraping) and returns both the **bias label** and **confidence score**.

---

## 🚀 Features

- 🤖 Fine-tuned `bert-base-uncased` model for text classification
- 🧠 Detects political bias: **Left**, **Center**, or **Right**
- 🌐 Web interface built with **HTML**, **CSS**, and **JavaScript**
- 🔗 Supports URL input with **web scraping** to extract news content
- 📊 Shows confidence score (bias intensity)
- ☁️ Deployable on platforms like **Render**, **Railway**, or **Heroku**

---

## 🧠 Model Details

- **Base Model:** `bert-base-uncased` from HuggingFace Transformers
- **Fine-tuned on:** 37,554 preprocessed news articles
- **Labels:** 
  - `0` - Left
  - `1` - Center
  - `2` - Right
- **Tokenization:** Using `AutoTokenizer` from HuggingFace
- **Loss Function:** CrossEntropyLoss
- **Optimizer:** AdamW

---

## 🖥️ Web App

### Frontend
- HTML + JavaScript interface
- Fetch API to communicate with the backend
- Displays predicted label and confidence

### Backend (Flask)
- `/predict` API route
- Accepts JSON input: `{ "text": "..." }`
- Returns response: 
  ```json
  {
    "label": "Right",
    "confidence": 0.92
  }
