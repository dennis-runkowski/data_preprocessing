""" Normalize Text - Remove Punctuation """
from string import punctuation
from data_preprocessing.steps.base import Steps


class RemovePunctuation(Steps):
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """
        Process item - remove unctuation from text
        Args:
            item (dict): item
        Returns:
            str: text with no punctuation
        """
        try:
            self.log.debug("Removing punctuation")
            remove_punctuation = str.maketrans('', '', punctuation)
            return item["data"].translate(remove_punctuation)
        except Exception as e:
            self.log.error(
                "Error removing punctuation from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]
