""" Base Class for all Steps. """

import hashlib

from data_preprocessing.utils.logger import setup_logging


class Steps:
    """ Base Steps Class """
    def __init__(self, config):
        """Initialize steps base class.

        Args:
            config (obj): config for the step
        """
        self.config = config
        self.log = self._logger()
        self.log.info("Initializing {} step".format(config['type']))

    def item_model(self, item):
        """Format each record into a standard item format.

        Each incoming record needs to be uniform. This method gets each item
        in the standard format for processing. Incoming item must be a dict and
        have the key data.

            Example Usage:
                record = {"id": 1, "data": "this is a test"}
                self.item_model(record)
        Args:
            item (dict): Dictionary containing the data

        Returns:
            Uniform dict with the necessary keys
        """
        if not isinstance(item, dict):
            self.log.error("Item is not in the correct format")
            return {}

        if "data" not in item.keys():
            self.log.error("Item is missing the data key")
            return {}

        formatted_item = {
            "id": "",
            "data": item["data"],
            "tags": {}
        }
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
            str
        """
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def _logger(self):
        """Helper function to setup the logger."""
        log = setup_logging(
            self.config["type"],
            self.config["log_level"]
        )
        return log
