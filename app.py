from flask import Flask, request, render_template
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['inputText']
    option = request.form['option']
    
    if option == 'Sentiment':
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(input_text)
        return render_template('index.html', sentiment_scores=sentiment_scores, input_text=input_text)
    
    return render_template('index.html', error_message="Invalid option selected.")

if __name__ == '__main__':
    app.run(debug=True)