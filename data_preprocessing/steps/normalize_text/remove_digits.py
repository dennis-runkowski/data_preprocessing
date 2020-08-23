""" Normalize Text - Remove Digits """
from string import digits
from data_preprocessing.steps.base import Steps


class RemoveDigits(Steps):
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """
        Process item - remove digits from text
        Args:
            item (dict): item
        Returns:
            str: text with no digits
        """
        try:
            self.log.debug("Removing digits")
            remove_digits = str.maketrans('', '', digits)
            return item["data"].translate(remove_digits)
        except Exception as e:
            self.log.error(
                "Error removing digits from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]
