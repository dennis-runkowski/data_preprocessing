""" Normalize Text - Remove Stop Words """
from data_preprocessing.steps.base import Steps


class RemoveStopWords(Steps):
    def __init__(self, config):
        super().__init__(config)
        if self.config.get("options") == "short_list":
            from data_preprocessing.steps.normalize_text.stop_words \
                import STOP_WORDS
            self.stop_words = STOP_WORDS
        elif self.config.get("options") == "long_list":
            from data_preprocessing.steps.normalize_text.stop_words \
                import STOP_WORDS_LONG
            self.stop_words = STOP_WORDS_LONG
        elif self.config.get("options") == "custom":
            self.stop_words = self.config.get("custom_list", [])

    def process(self, item):
        """
        Process item - remove stop words from text
        Args:
            item (dict): item
        Returns:
            str: text with no stop words
        """
        try:
            self.log.debug("Remove Stop Words Step - using {}".format(
                    self.config.get("options")
                )
            )
            item_text = item["data"].split(' ')
            item_text = [i for i in item_text if i not in self.stop_words]
            item_text = " ".join(item_text)

            return item_text
        except Exception as e:
            self.log.error(
                "Error removing stopwords from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]
