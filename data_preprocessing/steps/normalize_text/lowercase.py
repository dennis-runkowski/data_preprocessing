""" Normalize Text - Lower case """

from data_preprocessing.steps.base import Steps


class NormalizeLowerCase(Steps):
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """
        Process item - make text lowercase
        Args:
            item (dict): item
        Returns:
            str: lowercase text
        """
        try:
            item['data'] = item["data"].lower()
            self.log.debug("Converting to lowercase - {}".format(item['data']))
            return item['data']
        except Exception as e:
            self.log.error(
                "Error converting (item id:{}) to lowercase - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]
