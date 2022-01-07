""" Base Class for all Steps.

Steps are defined with a dictionary. Each step requires a key ('type'). The
type defines which step to use. Steps are used in the processing pipeline.
There are data loaders and normalize_text steps.
"""

import hashlib

from data_preprocessing.utils.logger import setup_logging


class Steps:
    """ Base Steps Class.

    Args:
        config (obj): config for the step
    """
    def __init__(self, config):
        """Initialize steps base class."""
        self._config = config
        self._log = self._logger()
        if self._config.get("name") not in ["tokenizer", "data_loader"]:
            self._tokenizer = self._config["tokenizer"]
        self._log.info("Initializing {} {}".format(
            config.get('type'),
            config.get('name')
            )
        )

    def _item_model(self, item, additional_keys=None):
        """Format each record into a standard item format.

        Each incoming record needs to be converted into the item model. The
        item model is a dictionary with three keys, id, data and tags.

        You can extend the item with the additional_keys arg.

        Args:
            item (dict): Dictionary containing the data
            additional_keys (list): Optional additional keys to add to the item
        Returns:
            dict: Containing the proper item format
        """
        if isinstance(item, str):
            item = {
                "data": item
            }
        elif not isinstance(item, dict):
            self._log.error("Item is not in the correct format")
            return {}

        if "data" not in item.keys():
            self._log.error("Item is missing the data key")
            return {}

        formatted_item = {
            "id": "",
            "data": item["data"],
            "tags": {}
        }
        if additional_keys:
            formatted_item["additional_keys"] = {}
            for key in additional_keys:
                formatted_item["additional_keys"][key] = item.get(key, "")

        if self._config["preserve_original"]:
            formatted_item["original_data"] = item["data"]

        if not item.get("id"):
            formatted_item["id"] = self._create_id(item["data"])
        else:
            formatted_item["id"] = item["id"]

        return formatted_item

    def _create_id(self, text):
        """Create unique id from text.

        Args:
            text (str): Text for the item
        Returns:
            str: Id created from hashing the text
        """
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def _logger(self):
        """Helper function to setup the logger."""
        log = setup_logging(
            self._config["type"],
            self._config.get("log_level")
        )
        return log
