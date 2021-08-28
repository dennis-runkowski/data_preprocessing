from time import process_time
import unittest

from data_preprocessing.steps.data_loaders.single_item import SingleItemLoader
from data_preprocessing.steps.data_loaders.list_loader import ListDataLoader
from data_preprocessing.steps.data_loaders.csv_loader import CsvDataLoader


TEST_DATA = "This is a TEST sentence!"
TEST_LIST = ['this is a test', 'I like dogs', "The jets suck."]


class TestDataLoaders(unittest.TestCase):

    def test_single_item(self):
        loader = SingleItemLoader()
        process = loader.process(TEST_DATA)
        self.assertEqual(TEST_DATA, process["data"])

    def test_list_loader(self):
        loader = ListDataLoader()
        data = []
        for batch in loader.process(TEST_LIST):
            data.append(batch['data'])
        self.assertEqual(TEST_LIST, data)

    def test_csv_loader(self):
        config = {
            "name": "data_loader",
            "type": "csv",
            "file_path": "test_data/test.csv",
            "columns": {
                "id": "id",
                "data": "text",
                "additional_columns": ["username"]
            },
            "batch_size": 1000,
            "log_level": "INFO",
            "preserve_original": False
        }
        loader = CsvDataLoader(config)
        data = [item['data'] for item in loader.process()]
        self.assertEqual(4, len(data))

if __name__ == "__main__":
    unittest.main()
    # pass