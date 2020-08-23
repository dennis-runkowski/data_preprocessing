""" Load Normalize Text Class"""

import importlib
import inspect

valid_types = {
    "lowercase": {
        "path": "data_preprocessing.steps.normalize_text.lowercase",
        "class": "NormalizeLowerCase"
    },
    "remove_digits": {
        "path": "data_preprocessing.steps.normalize_text.remove_digits",
        "class": "RemoveDigits"
    },
    "remove_punctuation": {
        "path": "data_preprocessing.steps.normalize_text.remove_punctuation",
        "class": "RemovePunctuation"
    },
    "remove_stopwords": {
        "path": "data_preprocessing.steps.normalize_text.remove_stopwords",
        "class": "RemoveStopWords"
    },
    "remove_whitespace": {
        "path": "data_preprocessing.steps.normalize_text.remove_whitespace",
        "class": "RemoveWhiteSpace"
    },
    "remove_html": {
        "path": "data_preprocessing.steps.normalize_text.remove_html",
        "class": "RemoveHtml"
    },
    "porter_stemmer": {
        "path": "data_preprocessing.steps.normalize_text.porter_stemmer",
        "class": "Stemmer"
    },
    "lemmatizer": {
        "path": "data_preprocessing.steps.normalize_text.lemmatizer",
        "class": "Lemmatizer"
    }
}


def fetch(config):
    """
    Fetch the steps based on the config and return the object
    Args:
        config (obj): Object with config for steps
    Returns:
        obj .steps.base Steps
    """
    try:
        step_type = config.get("type")
        module = importlib.import_module(
            valid_types[step_type]["path"],
            "data_preprocessing"
        )
        obj = getattr(module, valid_types[step_type]["class"])
        if inspect.isclass(obj):
            return obj(config)
    except Exception as e:
        raise ImportError(
            "Could not import Class {} - {}".format(config.get("type"), e)
        )
