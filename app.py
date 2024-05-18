from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

app = Flask(__name__)

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
    aspect_summaries = generate_summary(aspect_scores)
    
    return render_template('index.html', sentiment_scores=sentiment_scores, 
                           textblob_polarity=textblob_polarity, textblob_subjectivity=textblob_subjectivity,
                           aspect_scores=aspect_scores, aspect_summaries=aspect_summaries, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)