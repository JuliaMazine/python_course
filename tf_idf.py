import os
import math
import nltk
import pickle

class TF_IDF:
    def __init__(self, corpus_path):
        self.documents = []
        self.corpus_size = 0
        self.term_idf = {}

        if os.path.isfile('idf.pkl'):
            with open('idf.pkl', 'rb') as f:
                self.term_idf = pickle.load(f)
        else:
            stopwords = nltk.corpus.stopwords.words('english')
            def process_text(text):
                tokens = nltk.word_tokenize(text.lower())
                tokens = [token for token in tokens if token not in stopwords and len(token) > 2]
                return tokens

            with open(corpus_path, 'w', encoding='utf-8') as f:
                for text_file in ['1.txt', '2.txt', '3.txt']:
                    with open(text_file, 'r', encoding='utf-8') as t:
                        text = t.read().replace('\n', ' ')
                        tokens = process_text(text)
                        self.documents.append(tokens)
                        self.corpus_size += 1
                        f.write(' '.join(tokens) + ' ')

            for document in self.documents:
                for token in set(document):
                    if token in self.term_idf:
                        self.term_idf[token] += 1
                    else:
                        self.term_idf[token] = 1

            for term in self.term_idf:
                self.term_idf[term] = math.log(self.corpus_size / (1 + self.term_idf[term]))

            with open('idf.pkl', 'wb') as f:
                pickle.dump(self.term_idf, f)

    def get_tf_idf(self, text):
        tokens = nltk.word_tokenize(text.lower())
        tf = {}
        for token in tokens:
            if token in tf:
                tf[token] += 1
            else:
                tf[token] = 1
        tfidf = {}
        for token in tf:
            if token in self.term_idf:
                tfidf[token] = tf[token] * self.term_idf[token]
        return tfidf.items()

tfidf = TF_IDF('corpus.txt')
text = 'Hello, friends! In the summer I want to'
print(list(tfidf.get_tf_idf(text)))
