""" Normalize Text - Remove Whitespace """
from string import whitespace
from data_preprocessing.steps.base import Steps


class RemoveWhiteSpace(Steps):
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """
        Process item - remove whitespace from text
        Args:
            item (dict): item
        Returns:
            str: text with no whitespace
        """
        try:
            self.log.debug("Removing whitespace")
            item_text = item["data"].strip()
            item_text = " ".join(item_text.split())
            return item_text
        except Exception as e:
            self.log.error(
                "Error removing whitespace from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]
