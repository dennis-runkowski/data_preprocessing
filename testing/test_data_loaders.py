"""Unit Tests for data loaders"""

import unittest
from data_preprocessing.base import DataPreprocess

GOOD_LIST_1 = {
    "data_loader": {
        "type": "list",
        "batch_size": 15
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}
GOOD_LIST_2 = {
    "data_loader": {
        "type": "list"
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}
GOOD_CSV_1 = {
    "data_loader": {
        "type": "csv",
        "file_path": "this is a test",
        "columns": {"id": "job_id", "data": "description"},
        "batch_size": 15
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}
BAD_LIST_1 = {
    "data_loader": {
        "type": "lit",
        "batch_size": 15
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}
BAD_CSV_1 = {
    "data_loader": {
        "type": "csv"
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}
BAD_CSV_2 = {
    "data_loader": {
        "type": "csv",
        "file_path": "this is a test",
        "columns": "test",
        "batch_size": 15
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}
BAD_CSV_3 = {
    "data_loader": {
        "type": "csv",
        "file_path": 10,
        "columns": {"id": "job_id", "data": "description"},
        "batch_size": 15
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}


class TestConfig(unittest.TestCase):
    def test_good_config(self):
        try:
            # Test valid data config
            DataPreprocess(GOOD_LIST_1, "WARN")
        except Exception as e:
            self.fail("GOOD_LIST_1 failed - {}".format(e))

        try:
            # Test valid data config
            DataPreprocess(GOOD_LIST_2, "WARN")
        except Exception as e:
            self.fail("GOOD_LIST_2 failed - {}".format(e))
        try:
            # Test valid data config
            DataPreprocess(GOOD_CSV_1, "WARN")
        except Exception as e:
            self.fail("GOOD_CSV_1 failed - {}".format(e))

    def test_bad_data(self):
        # Test for bad type name
        self.assertRaises(ValueError, DataPreprocess, BAD_LIST_1, "WARN")
        # Test for bad type name
        self.assertRaises(KeyError, DataPreprocess, BAD_CSV_1, "WARN")
        # Test for bad type name
        self.assertRaises(TypeError, DataPreprocess, BAD_CSV_2, "WARN")
        # Test for bad type name
        self.assertRaises(TypeError, DataPreprocess, BAD_CSV_3, "WARN")


if __name__ == "__main__":
    unittest.main()
