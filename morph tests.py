import unittest
import os
from morphologt import Corpus


class TestCorpus(unittest.TestCase):
    def setUp(self):
        self.corpus = Corpus()
        self.corpus.load(os.path.join('annot.opcorpora.no_ambig.xml'))

    def test_corpus_len(self):
        self.assertEqual(len(self.corpus), 9798)

    def test_sentence_len(self):
        sentence = self.corpus.get_sentence(0)
        self.assertEqual(len(sentence), 7)

    def test_wordform_grammems(self):
        self.assertListEqual(self.corpus.get_wordform(0, 1).get_grammems(), ['NOUN', 'inan', 'femn', 'sing', 'nomn'])

if __name__ == '__main__':
    unittest.main()