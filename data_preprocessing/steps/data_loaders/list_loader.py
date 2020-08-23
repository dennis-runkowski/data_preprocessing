""" List data loader """

from data_preprocessing.steps.base import Steps


class ListDataLoader(Steps):
    def __init__(self, config):
        super().__init__(config)

    def process(self, data):
        """
        Yield item
        Args:
            data (obj): data to process
        Yields:
            obj: item
        """

        if not isinstance(data, list):
            self.log.error("Bad data type passed to list loader")
            raise TypeError("Data must be a list!")

        for item in data:
            item = self._validate_item(item)
            if not item:
                self.log.warn("Skipping item - {}".format(item))
                continue
            yield item

    def _validate_item(self, item):
        """
        Internal method to validate the item is in the right
        format.

        Example:
            item = {
                "id": 1,
                "data": "data to process"
            }
        Args:
            item (dict): Item is a dictionary
        Returns:
            dict: item
        """
        if not isinstance(item, dict):
            return None
        if not item.get("id") or not item.get("data"):
            return None
        self.log.debug("Validated item structure- {}".format(item.get("id")))
        return item
