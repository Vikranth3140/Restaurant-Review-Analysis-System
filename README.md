# Sentiment Analysis Platform

Sentiment Analysis Platform is a Flask-based web application that offers sentiment analysis functionality using the [Natural Language Toolkit (NLTK)](https://www.nltk.org/) and [TextBlob](https://textblob.readthedocs.io/en/dev/) in Python. This application allows users to analyze the sentiment of input text, providing detailed insights into its positive, negative, neutral, and compound sentiment scores.

The user interface is designed with simplicity in mind, utilizing [Bootstrap CSS](https://getbootstrap.com/) to ensure a clean and responsive design.

Live Demo ---> [Render](https://sentiment-analysis-platform.onrender.com)

![intro img](img\intro.png)


## Features

- **Sentiment Analysis**: Determines the sentiment of the input text (positive, negative, neutral) using VADER and TextBlob.
- **Polarity and Subjectivity**: Provides detailed polarity and subjectivity scores to indicate the sentiment strength and objectivity of the text.
- **Visualization**: Displays sentiment scores using interactive charts for better understanding.


### Sentiment Analysis Details


#### Positive, Negative, Neutral, and Compound Scores
- **Positive**: Indicates the proportion of positive sentiment in the text.
- **Negative**: Indicates the proportion of negative sentiment in the text.
- **Neutral**: Indicates the proportion of neutral sentiment in the text.
- **Compound**: A single score that combines the positive, negative, and neutral scores to provide an overall sentiment. It ranges from -1 (most extreme negative) to 1 (most extreme positive).

#### Polarity
- **Definition**: Polarity measures the sentiment expressed in a text, indicating whether the expressed opinion is positive, negative, or neutral.
- **Range**: The polarity score is a float within the range of -1.0 to 1.0.
  - **-1.0**: Indicates a very negative sentiment.
  - **0.0**: Indicates a neutral sentiment.
  - **1.0**: Indicates a very positive sentiment.
- **Interpretation**:
  - A polarity score closer to 1 indicates positive sentiment.
  - A polarity score closer to -1 indicates negative sentiment.
  - A polarity score around 0 indicates neutral sentiment.

#### Subjectivity
- **Definition**: Subjectivity measures the degree to which a text is subjective or objective.
- **Range**: The subjectivity score is a float within the range of 0.0 to 1.0.
  - **0.0**: Indicates the text is very objective.
  - **1.0**: Indicates the text is very subjective.
- **Interpretation**:
  - A subjectivity score closer to 1 indicates the text contains personal opinions, emotions, or judgments.
  - A subjectivity score closer to 0 indicates the text is more factual and objective.

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

    Sentiment-Analysis-Platform/
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
    git clone https://github.com/Vikranth3140/Sentiment-Analysis-Platform.git
    ```

2. Install the required Python dependencies.
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application.
    ```bash
    python app.py
    ```

4. Open the web interface in your browser (usually at `http://localhost:5000`).

5. Enter your text in the provided text box and click on `Analyze Sentiment` to see the results displayed on the web page.

## License

This project is licensed under the [MIT License](LICENSE).
