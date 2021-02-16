""" Normalize Text - Remove Stop Words """
from data_preprocessing.steps.base import Steps


class RemoveStopWords(Steps):
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
            str: text with no stop words
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
