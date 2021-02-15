""" Load Tokenizer Class"""

import importlib
import inspect
import uuid

valid_types = {
    "spaces": {
        "path": "data_preprocessing.steps.tokenizer.spaces",
        "class": "TokenizeSpaces"
    },
    "nltk_regex": {
        "path": "data_preprocessing.steps.tokenizer.nltk_regex",
        "class": "TokenizeNLTKRegex"
    },
    "nltk_word_tokenize": {
        "path": "data_preprocessing.steps.tokenizer.nltk_word_tokenize",
        "class": "TokenizeNLTKWord"
    },
    "spacy_word_tokenize": {
        "path": "data_preprocessing.steps.tokenizer.spacy_word_tokenize",
        "class": "TokenizeSpacyWord"
    }
}


def _fetch(config):
    """Fetch the steps based on the config and return the object.

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
