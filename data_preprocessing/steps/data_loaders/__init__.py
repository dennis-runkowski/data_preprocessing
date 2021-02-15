""" Load Data Loader Class"""

import importlib
import inspect
import uuid

valid_types = {
    "list": {
        "path": "data_preprocessing.steps.data_loaders.list_loader",
        "class": "ListDataLoader"
    },
    "csv": {
        "path": "data_preprocessing.steps.data_loaders.csv_loader",
        "class": "CsvDataLoader"
    },
    "single_item": {
        "path": "data_preprocessing.steps.data_loaders.single_item",
        "class": "SingleItemLoader"
    }
}


def _fetch(config):
    """Fetch the data_loader based on the config and return the object.

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
            "Could not import data loader Class - {}".format(e)
        )


def _create_id():
    """Create unique id.

    Returns:
        str: Random id as a string
    """
    return str(uuid.uuid1().int)
