"""Normalize Text - Remove Whitespace

Remove whitespace from a string of text. The config type must be set to
`remove_whitespace`.

Example:
    .. code-block::

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "list",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "remove_whitespace",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = [" Remove the whitespace  \n        from string of   text "]
        for batch in process.process_data(data):
            print(batch)
"""
from string import whitespace
from data_preprocessing.steps.base import Steps


class RemoveWhiteSpace(Steps):
    """Remove Whitespace step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "remove_whitespace",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """Process item - remove whitespace from text

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Remove Whitespace Step")
            item_text = item["data"].strip()
            item_text = item_text.replace("\n", " ").replace("\r", " ")
            item_text = " ".join(item_text.split())
            item["data"] = item_text
        except Exception as e:
            self._log.error(
                "Error removing whitespace from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
