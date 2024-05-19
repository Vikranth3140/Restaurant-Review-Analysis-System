from flask import Flask, request, render_template, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk
import datetime
import pandas as pd
import plotly.express as px
import os

# Download necessary NLTK data
nltk.download('vader_lexicon')

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

reviews = []

def analyze_aspects(text):
    aspects = {
        'service': ['service', 'waiter', 'waitress', 'staff', 'attentive', 'friendly', 'rude', 'slow'],
        'food': ['food', 'meal', 'dish', 'taste', 'appetizer', 'main course', 'dessert', 'flavor', 'overcooked'],
        'ambiance': ['ambiance', 'atmosphere', 'environment', 'decor', 'music', 'lighting', 'cozy', 'noisy', 'comfortable']
    }
    aspect_scores = {aspect: {'pos': 0, 'neg': 0, 'neu': 0, 'compound': 0} for aspect in aspects}
    sid = SentimentIntensityAnalyzer()
    
    for aspect, keywords in aspects.items():
        for keyword in keywords:
            if keyword in text.lower():
                scores = sid.polarity_scores(text)
                for key in scores:
                    aspect_scores[aspect][key] += scores[key]
    
    return aspect_scores

def generate_summary(aspect_scores):
    summaries = {}
    for aspect, scores in aspect_scores.items():
        if scores['compound'] >= 0.05:
            summaries[aspect] = f"The sentiment towards {aspect} is generally positive."
        elif scores['compound'] <= -0.05:
            summaries[aspect] = f"The sentiment towards {aspect} is generally negative."
        else:
            summaries[aspect] = f"The sentiment towards {aspect} is neutral."
    return summaries

@app.route('/')
def index():
    return render_template('index.html', reviews=reviews)

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['inputText']
    
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(input_text)
    textblob_analysis = TextBlob(input_text)
    textblob_polarity = textblob_analysis.sentiment.polarity
    textblob_subjectivity = textblob_analysis.sentiment.subjectivity
    aspect_scores = analyze_aspects(input_text)
    aspect_summaries = generate_summary(aspect_scores)
    
    review = {
        'text': input_text,
        'sentiment_scores': sentiment_scores,
        'textblob_polarity': textblob_polarity,
        'textblob_subjectivity': textblob_subjectivity,
        'aspect_scores': aspect_scores,
        'aspect_summaries': aspect_summaries,
        'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    reviews.append(review)
    
    return render_template('index.html', sentiment_scores=sentiment_scores, 
                           textblob_polarity=textblob_polarity, textblob_subjectivity=textblob_subjectivity,
                           aspect_scores=aspect_scores, aspect_summaries=aspect_summaries, input_text=input_text,
                           reviews=reviews)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            process_file(file_path)
            return render_template('index.html', reviews=reviews)
    return render_template('upload.html')

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                sid = SentimentIntensityAnalyzer()
                sentiment_scores = sid.polarity_scores(line)
                textblob_analysis = TextBlob(line)
                textblob_polarity = textblob_analysis.sentiment.polarity
                textblob_subjectivity = textblob_analysis.sentiment.subjectivity
                aspect_scores = analyze_aspects(line)
                aspect_summaries = generate_summary(aspect_scores)
                
                review = {
                    'text': line,
                    'sentiment_scores': sentiment_scores,
                    'textblob_polarity': textblob_polarity,
                    'textblob_subjectivity': textblob_subjectivity,
                    'aspect_scores': aspect_scores,
                    'aspect_summaries': aspect_summaries,
                    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                reviews.append(review)

@app.route('/dashboard')
def dashboard():
    df = pd.DataFrame(reviews)
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        fig = px.line(df, x='date', y=[review['sentiment_scores']['compound'] for review in reviews], title='Sentiment Over Time')
        graphJSON = fig.to_json()
    else:
        graphJSON = None
    return render_template('dashboard.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)