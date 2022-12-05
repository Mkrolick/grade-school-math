from sent2vec.vectorizer import Vectorizer

sentences = [
    "This is an awesome book to learn NLP.",
    "DistilBERT is an amazing NLP model.",
    "We can interchangeably use embedding, encoding, or vectorizing.",
]
vectorizer = Vectorizer()
vectorizer.run(sentences)
vectors = vectorizer.vectors

# documentation: https://pypi.org/project/sent2vec/
# run(sentences, remove_stop_words = ['not'], add_stop_words = [])