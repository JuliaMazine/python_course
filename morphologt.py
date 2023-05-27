import xml.etree.ElementTree as ET


class Wordform:
    def __init__(self, text, grammems):
        self._text = text
        self._grammems = grammems

    def get_text(self):
        return self._text

    def get_grammems(self):
        return self._grammems


class Sentence:
    def __init__(self, text, words):
        self._text = text
        self._words = words

    def get_text(self):
        return self._text

    def get_word(self, idx):
        return self._words[idx]

    def __len__(self):
        return len(self._words)


class Corpus:
    def __init__(self):
        self._sentences = []

    def get_sentence(self, idx):
        return self._sentences[idx]

    def get_wordform(self, sent_idx, word_idx):
        return self._sentences[sent_idx].get_word(word_idx)

    def get_grammems(self, sent_idx, word_idx):
        return self._sentences[sent_idx].get_word(word_idx).get_grammems()

    def load(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        for sent_node in root.iter('sentence'):
            text = sent_node.find('source').text
            words = []
            for token_node in sent_node.findall('tokens/token'):
                text = token_node.get('text')
                grammems = []
                for gram_node in token_node.iter('g'):
                    grammems.append(gram_node.attrib['v'])
                wordform = Wordform(text, grammems)
                words.append(wordform)
            sentence = Sentence(text, words)
            self._sentences.append(sentence)

    def __len__(self):
        return len(self._sentences)



