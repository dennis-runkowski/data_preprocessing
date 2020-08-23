""" Load Data Loader Class"""

import importlib
import inspect

valid_types = {
    "list": {
        "path": "data_preprocessing.steps.data_loaders.list_loader",
        "class": "ListDataLoader"
    },
    "csv": {
        "path": "data_preprocessing.steps.data_loaders.csv_loader",
        "class": "CsvDataLoader"
    }
}


def fetch(config):
    """
    Fetch the data_loader based on the config and return the object
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
            "Could not import data loader Class - {}".format(e)
        )
