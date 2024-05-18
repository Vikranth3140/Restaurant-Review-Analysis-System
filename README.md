# NLTK Web App

NLTK Web App is a Flask web application provides various natural language processing (NLP) functionalities using [NLTK (Natural Language Toolkit)](https://www.nltk.org/) in Python. It allows users to perform tasks such as tokenization, POS tagging, named entity recognition (NER), sentiment analysis, word frequency analysis, concordance, WordNet integration, and chunking on input text.

Please note that the UI is kept relatively simpler with [Bootstrap CSS](https://getbootstrap.com/).

Live Demo ---> [Render](https://nltk-web-app.onrender.com)


## Features

- **Tokenization**: Breaks input text into individual tokens or words.
- **Stopwords Removal**: Filters out common stopwords from the input text.
- **POS Tagging**: Assigns parts of speech tags to tokens (e.g., nouns, verbs, adjectives).
- **Named Entity Recognition (NER)**: Identifies named entities such as persons, organizations, and locations.
- **Sentiment Analysis**: Determines the sentiment of the input text (positive, negative, neutral).
- **Word Frequency Analysis**: Counts the frequency of words in the input text.
- **Concordance**: Finds and displays contexts surrounding a specified keyword in the input text.
- **WordNet Integration**: Retrieves information about words from WordNet, including definitions, examples, hypernyms, hyponyms, holonyms, and meronyms.
- **Chunking**: Groups tokens into chunks based on specified patterns (e.g., noun phrases).


## Example Usage

- **Tokenization:**
  - **Input:** "NLTK Web App is awesome."
  - **Output:** "NLTK Web App is awesome."

- **Stopwords Removal:**
  - **Input:** "NLTK Web App is awesome."
  - **Output:** "NLTK Web App awesome."

- **POS Tagging:**
  - **Input:** "NLTK Web App is awesome."
  - **Output:** "NLTK (NNP) Web (NNP) App (NNP) is (VBZ) awesome (JJ) . (.)"

- **NER:**
  - **Input:** "NLTK Web App is developed by John Doe."
  - **Output:** "PERSON: John Doe"

- **Sentiment Analysis:**
  - **Input:** "NLTK Web App is awesome."
  - **Output:** "Positive: 1.0, Negative: 0.0, Neutral: 0.0, Compound: 0.6249"

- **Word Frequency Analysis:**
  - **Input:** "NLTK Web App is awesome. NLTK is powerful."
  - **Output:** "NLTK: 2, Web: 1, App: 1, awesome: 1, powerful: 1"

- **Concordance:**
  - **Input:** "NLTK Web App is awesome."
  - **Keyword:** "Web"
  - **Output:** "NLTK Web App"

- **WordNet Integration:**
  - **Input:** "awesome"
  - **Output:** 
    - **Definition:** "extremely impressive or daunting; inspiring awe."
    - **Examples:** "the awesome power of the atomic bomb"
    - **Hypernyms:** "impressive"
    - **Hyponyms:** "amazing, awful, awing"
    - **Holonyms:** ""
    - **Meronyms:** ""

- **Chunking:**
  - **Input:** "The quick brown fox jumps over the lazy dog."
  - **Output:** (S (NP The/DT quick/JJ brown/JJ fox/NN) (VP jumps/VBZ) (PP over/IN) (NP the/DT lazy/JJ dog/NN) ./.)


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

5. Enter text in the input field and choose the desired NLP task from the dropdown menu.

6. Submit the form to see the results displayed on the web page.


## License

This project is licensed under the [MIT License](LICENSE).
