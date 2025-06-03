from flask import Flask, request, jsonify, send_from_directory
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import validators
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = AutoModelForSequenceClassification.from_pretrained("./new_model")
tokenizer = AutoTokenizer.from_pretrained("./new_model")

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        return ' '.join(p.get_text() for p in paragraphs)
    except Exception as e:
        return str(e)

@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'app.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_type = data.get("inputType")
    text = data.get("text", "")

    if input_type == "url":
        if not validators.url(text):
            return jsonify({"error": "Invalid URL"}), 400
        text = extract_text_from_url(text)
        if not text:
            return jsonify({"error": "Failed to extract text from the URL"}), 500

    if not text:
        return jsonify({"error": "No text provided"}), 400

    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)[0]

    label = torch.argmax(probabilities).item()
    confidence = probabilities[label].item()
    labels = ["Left", "Center", "Right"]

    return jsonify({"label": labels[label], "confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)
