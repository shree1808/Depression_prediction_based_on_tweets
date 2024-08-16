from flask import Flask, request, jsonify, render_template
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load your model
model = joblib.load('Notebook/RF_model.pkl')
vectorizer = joblib.load('Notebook/vectorizer.pkl')


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

    
def analyze_text(text):
    preprocessed_text = preprocess_text(text)
    text_vector = vectorizer.transform([preprocessed_text])
    prediction = model.predict(text_vector)
    return prediction[0]

@app.route('/')
def home():
    return "NLP Model API"

@app.route('/predict', methods=['GET', 'POST'])
def analyze():
    prediction = None
    if request.method == 'POST':
        text = request.form['text']
        prediction = analyze_text(text)
    return render_template('index.html', prediction = prediction)

if __name__ == '__main__':
    app.run(debug=True)
