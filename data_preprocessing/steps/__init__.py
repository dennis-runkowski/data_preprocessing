""" Fetch Steps """

import importlib
import inspect

valid_steps = {
    "normalize_text": "data_preprocessing.steps.normalize_text",
    "tokenizer": "data_preprocessing.steps.tokenizer",
    "data_loader": "data_preprocessing.steps.data_loaders"
}


def _fetch(config):
    """Fetch the steps based on the config and return the object.

    Args:
        config (obj): Object with config for steps
    Returns:
        obj data_preprocessing.steps.base Steps
    """
    try:
        step_name = config.get("name")
        module = importlib.import_module(
            valid_steps.get(step_name),
            "data_preprocessing"
        )
        return module._fetch(config)
    except Exception as e:
        raise ImportError(
            "Could not load module - {}".format(e)
        )
