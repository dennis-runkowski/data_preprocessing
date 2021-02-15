"""Normalize Text - Remove punctuation

Remove punctuation from a string of text. This step can not run before the
steps `remove_html` or `remove_urls`.The config type must be set to
`remove_punctuation`.

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
                    "type": "remove_punctuation",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = ["Why am I a jets fan?"]
        for batch in process.process_data(data):
            print(batch)
"""
from string import punctuation
from data_preprocessing.steps.base import Steps


class RemovePunctuation(Steps):
    """Remove Punctuation step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "remove_punctuation",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """Process item - remove punctuation from text

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Remove Punctuation Step")
            remove_punctuation = str.maketrans(
                punctuation, ' '*len(punctuation)
            )
            item["data"] = item["data"].translate(remove_punctuation)
        except Exception as e:
            self._log.error(
                "Error removing punctuation from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
