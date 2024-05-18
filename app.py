from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
from nltk.chunk import RegexpParser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet as wn
from collections import defaultdict, Counter

app = Flask(__name__)

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')
nltk.download('wordnet')

def generate_concordance(tokens, keyword, window_size=3):
    concordance_list = []
    for i, token in enumerate(tokens):
        if token.lower() == keyword.lower():
            start_index = max(0, i - window_size)
            end_index = min(len(tokens), i + window_size + 1)
            context = ' '.join(tokens[start_index:end_index])
            concordance_list.append(context)
    return concordance_list

def get_wordnet_info(word):
    synsets = wn.synsets(word)
    if synsets:
        synset = synsets[0]  # Taking the first synset for simplicity
        return {
            'Definition': synset.definition(),
            'Examples': synset.examples(),
            'Hypernyms': synset.hypernyms(),
            'Hyponyms': synset.hyponyms(),
            'Holonyms': synset.member_holonyms(),
            'Meronyms': synset.part_meronyms()
        }
    else:
        return None

def generate_chunks(tagged_tokens):
    grammar = r"""
        NP: {<DT>?<JJ>*<NN>}  # Chunk sequences of DT, JJ, NN
            {<NNP>+}          # Chunk consecutive proper nouns
    """
    chunk_parser = RegexpParser(grammar)
    tree = chunk_parser.parse(tagged_tokens)
    return tree

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['inputText']
    option = request.form['option']
    keyword = request.form.get('keyword')

    if not input_text.strip():  # Check if input text is empty or contains only whitespace
        return render_template('index.html', error_message='Input text cannot be empty.')

    # Tokenization and stopwords removal
    tokens = word_tokenize(input_text)
    if not tokens:  # Check if tokenization produced any tokens
        return render_template('index.html', error_message='Error in tokenization.')

    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    tokenized_text = ' '.join(filtered_tokens)

    # POS Tagging
    tagged_tokens = pos_tag(filtered_tokens)
    pos_tagged_text = ' '.join([f'{token} ({tag})' for token, tag in tagged_tokens])

    # Named Entity Recognition (NER)
    ner_result = defaultdict(list)
    ne_tree = ne_chunk(tagged_tokens)
    for subtree in ne_tree:
        if isinstance(subtree, nltk.tree.Tree):
            entity = ' '.join([token for token, tag in subtree.leaves()])
            label = subtree.label()
            ner_result[label].append(entity)

    # Sentiment Analysis
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(input_text)

    # Word Frequency Analysis
    word_freq = Counter(filtered_tokens)

    # Concordance
    concordance_list = generate_concordance(filtered_tokens, keyword)

    # WordNet Integration
    wordnet_info = get_wordnet_info(keyword)

    # Chunking
    chunked_tree = generate_chunks(tagged_tokens)

    if option == 'Tokenize':
        return render_template('index.html', tokenized_text=tokenized_text)
    elif option == 'PosTag':
        return render_template('index.html', pos_tagged_text=pos_tagged_text)
    elif option == 'NER':
        return render_template('index.html', ner_result=ner_result)
    elif option == 'Sentiment':
        return render_template('index.html', sentiment_scores=sentiment_scores)
    elif option == 'WordFreq':
        return render_template('index.html', word_freq=word_freq.most_common())
    elif option == 'Concordance':
        return render_template('index.html', concordance_list=concordance_list, keyword=keyword)
    elif option == 'WordNet':
        return render_template('index.html', wordnet_info=wordnet_info, keyword=keyword)
    elif option == 'Chunking':
        return render_template('index.html', chunked_tree=chunked_tree)
    elif option == 'All':
        return render_template('index.html', tokenized_text=tokenized_text, pos_tagged_text=pos_tagged_text,
                               ner_result=ner_result, sentiment_scores=sentiment_scores,
                               word_freq=word_freq.most_common(), concordance_list=concordance_list,
                               wordnet_info=wordnet_info, chunked_tree=chunked_tree, keyword=keyword)
    else:
        return render_template('index.html')  # Default render without results

if __name__ == '__main__':
    app.run(debug=True)