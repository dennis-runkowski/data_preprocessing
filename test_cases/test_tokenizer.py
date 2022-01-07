import unittest

from data_preprocessing.steps.tokenizer.nltk_regex import TokenizeNLTKRegex
from data_preprocessing.steps.tokenizer.nltk_word_tokenize import \
    TokenizeNLTKWord
from data_preprocessing.steps.tokenizer.spaces import TokenizeSpaces
from data_preprocessing.steps.tokenizer.spacy_word_tokenize import \
    TokenizeSpacyWord

TEST_DATA = "This isn't a TEST sentences!"


class TestTokenizer(unittest.TestCase):
    def test_nltk_regex(self):
        config = {
            "name": "tokenizer",
            "type": "nltk_regex",
            "log_level": "INFO"
        }
        data = {
            "data": TEST_DATA,
            "id": "1234"
        }
        tokenizer = TokenizeNLTKRegex(config)
        test = tokenizer.process(data)
        self.assertEqual(5, len(test["data"]))

    def test_nltk_word(self):
        config = {
            "name": "tokenizer",
            "type": "nltk_word_tokenize",
            "log_level": "INFO"
        }
        data = {
            "data": TEST_DATA,
            "id": "1234"
        }
        tokenizer = TokenizeNLTKWord(config)
        test = tokenizer.process(data)
        self.assertEqual(7, len(test["data"]))

    def test_spaces(self):
        config = {
            "name": "tokenizer",
            "type": "spaces",
            "log_level": "INFO"
        }
        data = {
            "data": TEST_DATA,
            "id": "1234"
        }
        tokenizer = TokenizeSpaces(config)
        test = tokenizer.process(data)
        self.assertEqual(5, len(test["data"]))

    def test_spacy(self):
        config = {
            "name": "tokenizer",
            "type": "spacy_word_tokenize",
            "log_level": "INFO"
        }
        data = {
            "data": TEST_DATA,
            "id": "1234"
        }
        tokenizer = TokenizeSpacyWord(config)
        test = tokenizer.process(data)
        self.assertEqual(7, len(test["data"]))


if __name__ == "__main__":
    unittest.main()
