import unittest
from tf_idf import TF_IDF
import math

class TestTFIDF(unittest.TestCase):
    def setUp(self):
        self.tfidf = TF_IDF()

    def test_tf_idf_calculation(self):
        text = "This is the first document. It contains words, phrases and sentences."
        expected_tfidf = {('contains', 0.0), ('document', 0.6931471805599453), ('phrases', 0.0), ('sentences', 0.0), ('words', 0.0), ('first', 0.6931471805599453)}
        self.assertSetEqual(set(self.tfidf.get_tf_idf(text)), expected_tfidf)

    def test_corpus_size(self):
        self.assertEqual(self.tfidf._corpus_size, 3)


    def test_word_frequency(self):
        self.assertEqual(self.tfidf._term_idf['sentences'], math.log(3 / 2))


if __name__ == '__main__':
    unittest.main()

