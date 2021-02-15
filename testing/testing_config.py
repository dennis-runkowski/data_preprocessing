import unittest
from data_preprocessing.base import DataPreprocess

bad_config = {
    "data1": {
        "name": "data_loader",
        "type": "list",
        "batch_size": 10
    },
    "steps": [{
        "name": "normalize_text",
        "type": "lowercase"
    }]
}
good_config = {
    "data": {
        "name": "data_loader",
        "type": "list",
        "batch_size": 10
    },
    "steps": [{
        "name": "normalize_text",
        "type": "lowercase"
    }]
}
bad_steps_1 = {
    "data": {
        "name": "data_loader",
        "type": "list",
        "batch_size": 10
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lower case"
        }
    ]
}
bad_steps_2 = {
    "data": {
        "name": "data_loader",
        "type": "list",
        "batch_size": 10
    },
    "steps": {
        "name": "normalize_text",
        "type": "lowercase"
    }
}
bad_steps_3 = {
    "data": {
        "name": "data_loader",
        "type": "list",
        "batch_size": 10
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "remove_stopwords"
        },
        {
            "name": "normalize_text",
            "type": "lowercase"
        }
    ]
}
good_steps = {
    "data": {
        "name": "data_loader",
        "type": "list",
        "batch_size": 10
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase"
        },
        {
            "name": "normalize_text",
            "type": "remove_stopwords"
        }
    ]
}


class TestConfig(unittest.TestCase):
    def test_bad_config(self):
        # Test for missing data key
        self.assertRaises(KeyError, DataPreprocess, bad_config, "WARN")

    def test_good_config(self):
        try:
            # Test valid data config
            DataPreprocess(good_config, "WARN")
        except Exception as e:
            self.fail("Not excepting good config! - {}".format(e))

    def test_steps_1(self):
        # Test for bad step name
        self.assertRaises(ValueError, DataPreprocess, bad_steps_1, "WARN")

    def test_steps_2(self):
        # Test for bad steps format
        self.assertRaises(TypeError, DataPreprocess, bad_steps_2, "WARN")

    def test_steps_3(self):
        # Test for missing required step (stopwords needs lowercase)
        self.assertRaises(KeyError, DataPreprocess, bad_steps_3, "WARN")

    def test_good_steps(self):
        try:
            # Test valid steps config
            DataPreprocess(good_steps, "WARN")
        except Exception as e:
            self.fail("Not excepting good steps! - {}".format(e))


if __name__ == "__main__":
    unittest.main()
