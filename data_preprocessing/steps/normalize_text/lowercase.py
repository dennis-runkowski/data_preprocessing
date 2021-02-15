"""Normalize Text - Lowercase step.

Convert all the text to lowercase form. The config type must be set to
`lowercase`.

Example:
    .. code-block::

        from data_preprocessing.base import DataPreprocess

        config = {
            "data_loader": {
                "type": "list",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = ["THIS IS A TEST sentence."]
        for batch in process.process_data(data):
            print(batch)
"""
from data_preprocessing.steps.base import Steps


class NormalizeLowerCase(Steps):
    """Lowercase step class.

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "lowercase",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        if self._config["type"] != "lowercase":
            self._log.error("Config type does not match!")
            raise ValueError("Bad config type value.")

    def process(self, item):
        """Process item - Convert item data lowercase.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Lowercase Step")
            item["data"] = item["data"].lower()
        except Exception as e:
            self._log.error(
                "Error converting (item id:{}) to lowercase - {}".format(
                    item["id"],
                    e
                )
            )
        return item
