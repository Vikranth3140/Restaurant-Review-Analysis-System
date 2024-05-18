# NLTK Web App

NLTK Web App is a Flask web application provides various natural language processing (NLP) functionalities using [NLTK (Natural Language Toolkit)](https://www.nltk.org/) in Python. It allows users to perform tasks such as tokenization, POS tagging, named entity recognition (NER), sentiment analysis, word frequency analysis, concordance, WordNet integration, and chunking on input text.

Please note that the UI is kept relatively simpler with [Bootstrap CSS](https://getbootstrap.com/).

Live Demo ---> [Render](https://nltk-web-app.onrender.com)


## Features

- **Sentiment Analysis**: Determines the sentiment of the input text (positive, negative, neutral).


## Example Usage

1. **Positive Sentiment**:
   ```
   I had an amazing experience at the new restaurant in town. The food was absolutely delicious, and the staff were incredibly friendly and attentive. The ambiance was perfect, with a cozy atmosphere that made me feel right at home. I can't wait to go back again soon!
   ```

2. **Negative Sentiment**:
   ```
   I had a terrible experience at the new restaurant in town. The food was bland and tasteless, and the staff were rude and inattentive. The ambiance was awful, with loud music and uncomfortable seating. I will never go back there again.
   ```

3. **Neutral Sentiment**:
   ```
   I visited the new restaurant in town. The food was okay, nothing special, but not bad either. The staff were decent and did their job. The ambiance was average, not too exciting but not uncomfortable. Overall, it was a typical dining experience.
   ```

4. **Mixed Sentiment**:
   ```
   I recently watched a movie that left me feeling very conflicted. On one hand, the acting was superb, and the cinematography was breathtaking. The lead actor delivered an outstanding performance that truly brought the character to life. On the other hand, the storyline felt a bit disjointed and confusing at times. There were plot holes that were never addressed, and the ending left a lot to be desired. Overall, I have mixed feelings about the movie. While I enjoyed the visual and acting aspects, the story left me feeling unsatisfied.
   ```

5. **Positive with Subtle Negative Aspects**:
   ```
   The vacation to the mountains was wonderful. The scenery was breathtaking, and the weather was perfect. The only downside was the long drive to get there, which was a bit exhausting. However, the beautiful landscapes and fresh mountain air made it all worth it.
   ```

6. **Negative with Positive Aspects**:
   ```
   My experience with the customer service team was mostly frustrating. They were slow to respond and didn't resolve my issue initially. However, one representative was very helpful and eventually fixed the problem. Despite the overall poor service, I appreciated that individual’s effort.
   ```


## Project Structure

    NLTK-Web-App/
    │
    ├── app.py              # Flask application code
    ├── templates/          # HTML templates
    │   └── index.html      # Main page template
    ├── README.md           # Project overview and instructions
    └── requirements.txt    # Python dependencies


- `app.py`: Main Flask application file containing route definitions and NLP functionalities.
- `index.html`: HTML template for the web interface.
- `requirements.txt`: List of Python dependencies required to run the application.


## How to Use

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/Vikranth3140/NLTK-Web-App.git
    ```

2. Install the required Python dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application with
    ```bash
    python app.py
    ```

4. Open the web interface in your browser (usually at `http://localhost:5000`).

5. Click on `Analyze Sentiment` to see the results displayed on the web page.


## License

This project is licensed under the [MIT License](LICENSE).