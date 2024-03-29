"""Process data from a list.

This data loader processes data from an in memory list, formats the data to the
item model and processes through the data preprocessing pipeline. An id is
generated by hashing the text.

Example:
    .. code-block::

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "list",
                "batch_size": 1000,
                "log_level": "INFO",
                "preserve_original": True # default is False
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO"
                },
            ]
        }
        loader = DataPreprocess(config, log_level='INFO')
        for batch in loader.process_data(data):
            print(batch)
            break

"""

from data_preprocessing.steps.base import Steps


class ListDataLoader(Steps):
    """List Data Loader class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            config = {
                "type": "list",
                "batch_size": 1000,
                "log_level": "INFO"
            }
    """
    def __init__(self, config=None):
        if not config:
            config = {
                "name": "data_loader",
                "type": "list",
                "batch_size": 1000,
                "log_level": "INFO",
                "preserve_original": False
            }
        super().__init__(config)

    def process(self, data):
        """ Process list of data.

        Transform into a valid item and yield the item.

        Args:
            data (list): data to process
        Yields:
            obj: item
        """

        if not isinstance(data, list):
            self._log.error("Bad data type passed to list loader")
            raise TypeError("Data must be a list!")

        for item in data:
            if isinstance(item, dict) or isinstance(item, list):
                self._log.warn("Skipping item bad format- {}".format(item))
                continue
            item = {
                "data": item
            }
            yield self._item_model(item)
