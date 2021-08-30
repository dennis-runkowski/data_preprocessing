from time import process_time
import unittest

from data_preprocessing import DataPreprocess
from data_preprocessing.utils.config_template import ConfigTemplates

templates = ConfigTemplates()

TEST_DATA = "This isn't a TEST sentences!"
TEST_LIST = ["this is a test", "I like dogs", "The jets suck."]


class TestNormalizer(unittest.TestCase):
    def test_lower(self):
        config = templates.pipeline()
        config['data_loader'] = templates.data_loader_single_item_loader()
        config['steps'].append(templates.normalize_text_lowercase())
        loader = DataPreprocess(config)
        process = loader.process_item(TEST_DATA)
        self.assertEqual(TEST_DATA.lower(), process["data"])

    def test_contractions(self):
        config = templates.pipeline()
        config['data_loader'] = templates.data_loader_single_item_loader()
        config['steps'].append(templates.normalize_text_lowercase())
        config['steps'].append(templates.normalize_text_expand_contractions())
        loader = DataPreprocess(config)
        process = loader.process_item(TEST_DATA)
        self.assertEqual("this is not a test sentences!", process["data"])

    def test_lemmatizer(self):
        config = templates.pipeline()
        config['data_loader'] = templates.data_loader_single_item_loader()
        config['steps'].append(templates.normalize_text_lowercase())
        config['steps'].append(templates.normalize_text_lemmatizer())
        loader = DataPreprocess(config)
        process = loader.process_item("How many cities are there?")
        self.assertEqual("how many city are there?", process["data"])

    def test_stemmer(self):
        config = templates.pipeline()
        config['data_loader'] = templates.data_loader_single_item_loader()
        config['steps'].append(templates.normalize_text_lowercase())
        config['steps'].append(templates.normalize_text_remove_punctuation())
        config['steps'].append(templates.normalize_text_porter_stemmer())
        loader = DataPreprocess(config)
        process = loader.process_item(TEST_DATA)
        self.assertEqual("thi isn t a test sentenc", process["data"])


if __name__ == "__main__":
    unittest.main()
