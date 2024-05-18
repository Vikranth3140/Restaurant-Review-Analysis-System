from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['inputText']
    option = request.form['option']

    if option == 'Sentiment':
        sentiment_scores = analyze_sentiment(text)
        return render_template('index.html', sentiment_scores=sentiment_scores)
    else:
        return render_template('index.html', error_message="Invalid option selected")

def analyze_sentiment(text):
    # Using VADER sentiment analysis
    sia = SentimentIntensityAnalyzer()
    vader_scores = sia.polarity_scores(text)

    # Using TextBlob sentiment analysis
    blob = TextBlob(text)
    textblob_sentiment = blob.sentiment

    return {
        'vader': vader_scores,
        'textblob': {
            'polarity': textblob_sentiment.polarity,
            'subjectivity': textblob_sentiment.subjectivity
        }
    }

if __name__ == '__main__':
    app.run(debug=True)