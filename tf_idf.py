import os
import math
import nltk
import pickle
from collections import Counter
class TF_IDF:
    def __init__(self):
        self._documents = []
        self._corpus_size = 0
        self._term_idf = {}

        if os.path.isfile('idf.pkl'):
            with open('idf.pkl', 'rb') as f:
                self._term_idf = pickle.load(f)
        else:
            stopwords = nltk.corpus.stopwords.words('english')

            for text_file in ['1.txt', '2.txt', '3.txt']:
                with open(text_file, 'r', encoding='utf-8') as t:
                    text = t.read().replace('\n', ' ')
                    tokens = nltk.word_tokenize(text.lower())
                    tf = Counter(token for token in tokens if token not in stopwords and len(token) > 2)
                    self._documents.append(tf)
                    self._corpus_size += 1

            for document in self._documents:
                for term, count in document.items():
                    if term in self._term_idf:
                        self._term_idf[term] += 1
                    else:
                        self._term_idf[term] = 1

            for term in self._term_idf:
                self._term_idf[term] = math.log(self._corpus_size / (1 + self._term_idf[term]))

            with open('idf.pkl', 'wb') as f:
                pickle.dump(self._term_idf, f)

    def get_tf_idf(self, text):
        tokens = nltk.word_tokenize(text.lower())
        tf = Counter(token for token in tokens if token in self._term_idf)
        tfidf = {}
        for token, count in tf.items():
            tfidf[token] = count * self._term_idf.get(token, 0)
        return tfidf.items()

