"""Normalize Text - Remove stop words

Remove stop words from a string of text. The lowercase step must be run before
this step to prevent duplicate processing. The config type must be set to
`remove_stopwords`. You can use the options argument to use the short, long or
a custom list of stop words. The default is the short list.

Example:
    .. code-block::

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "single_item",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO",
                }
                {
                    "name": "normalize_text",
                    "type": "remove_stopwords",
                    "options": "long_list",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = "sentences TO CleAn with some stop words!"
        data = process.process_item(data)
"""
from data_preprocessing.steps.base import Steps


class RemoveStopWords(Steps):
    """Remove Stopwords step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "remove_stopwords",
                "options": "long_list",  # optional
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        options = self._config.get("options")
        if options == "long_list":
            from data_preprocessing.steps.normalize_text.stop_words \
                import STOP_WORDS_LONG
            self._stop_words = STOP_WORDS_LONG
        elif options == "custom":
            custom_list = self._config.get("custom_list")
            if not custom_list:
                raise KeyError("Missing custom_list key")
            if not isinstance(custom_list, list):
                raise TypeError("custom_list must be a list of stop words")
            self._stop_words = custom_list
        else:
            from data_preprocessing.steps.normalize_text.stop_words \
                import STOP_WORDS
            self._stop_words = STOP_WORDS

    def process(self, item):
        """
        Process item - remove stop words from text

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Remove Stop Words Step - using {}".format(
                    self._config.get("options")
                )
            )
            item = self._tokenizer.process(item)
            item_text = [i for i in item["data"] if i not in self._stop_words]
            item_text = " ".join(item_text)
            item["data"] = item_text
        except Exception as e:
            self._log.error(
                "Error removing stopwords from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
