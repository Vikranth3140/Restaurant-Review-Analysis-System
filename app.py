from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

app = Flask(__name__)

def analyze_aspects(text):
    aspects = {
        'service': ['service', 'waiter', 'waitress', 'staff'],
        'food': ['food', 'meal', 'dish', 'taste'],
        'ambiance': ['ambiance', 'atmosphere', 'environment', 'decor']
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['inputText']
    
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(input_text)
    textblob_analysis = TextBlob(input_text)
    textblob_polarity = textblob_analysis.sentiment.polarity
    textblob_subjectivity = textblob_analysis.sentiment.subjectivity
    aspect_scores = analyze_aspects(input_text)
    
    return render_template('index.html', sentiment_scores=sentiment_scores, 
                           textblob_polarity=textblob_polarity, textblob_subjectivity=textblob_subjectivity,
                           aspect_scores=aspect_scores, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)