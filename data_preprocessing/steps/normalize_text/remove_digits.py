"""Normalize Text - Remove digits

Remove digits from a string of text. The config type must be set to
`remove_digits`.

Example:
    .. code-block::

        from data_preprocessing.base import DataPreprocess

        config = {
            "data_loader": {
                "type": "single_item",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "remove_digits",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = "The year is 2021"
        data = process.process_item(data)
"""
from string import digits
from data_preprocessing.steps.base import Steps


class RemoveDigits(Steps):
    """Remove Digits step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "remove_digits",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """Process item - remove digits from text

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Remove Digits Step")
            remove_digits = str.maketrans('', '', digits)
            item["data"] = item["data"].translate(remove_digits)
        except Exception as e:
            self._log.error(
                "Error removing digits from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
