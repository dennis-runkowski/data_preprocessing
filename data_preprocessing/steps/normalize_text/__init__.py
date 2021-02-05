""" Load Normalize Text Class"""

import importlib
import inspect
import uuid

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
    },
    "debugger_step": {
        "path": "data_preprocessing.steps.normalize_text.debugger_step",
        "class": "DebuggerStep"
    },
    "expand_contractions": {
        "path": "data_preprocessing.steps.normalize_text.expand_contractions",
        "class": "ExpandContractions"
    },
    "custom_normalize": {
        "path": "data_preprocessing.steps.normalize_text.custom_normalize",
        "class": "CustomNormalize"
    },
    "remove_urls": {
        "path": "data_preprocessing.steps.normalize_text.remove_urls",
        "class": "RemoveUrls"
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
        class_name = "{c}_{i}".format(
            c=valid_types[step_type]["class"],
            i=_create_id()
        )
        obj = type(
            class_name,
            (getattr(module, valid_types[step_type]["class"]),),
            {}
        )
        if inspect.isclass(obj):
            return obj(config)
    except Exception as e:
        raise ImportError(
            "Could not import Class {} - {}".format(config.get("type"), e)
        )


def _create_id():
    """Create unique id.

    Returns:
        str: Random id as a string
    """
    return str(uuid.uuid1().int)
