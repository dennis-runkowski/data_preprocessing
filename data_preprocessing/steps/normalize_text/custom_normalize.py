""" Normalize Text - Custom normalize step.

This class is used to add a custom step to the pipeline. In order to use this
you must create a class with a method called process that takes one argument
for the data. You must return the item in order for it to finish through the
remainder of the pipeline. In your config you must add the key `custom_class`
that contains the custom class object. The config type must be set to
`custom_normalize`

Example:
    .. code-block::

        # Create a custom class with the method process
        class CustomClass:
            def process(self, item):
                item['data'] = item['data'].upper()
                return item

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "single_item",
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "custom_normalize",
                    "log_level": "INFO",
                    "custom_class": CustomClass()
                }
            ]
        }
        process = DataPreprocess(config)
        data = "sentences TO CleAn!"
        data = process.process_item(data):
"""
import importlib
from data_preprocessing.steps.base import Steps


class CustomNormalize(Steps):
    """Debugger step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "custom_normalize",
                "log_level": "INFO"
                "custom_class": CustomClass()
            }
    """
    def __init__(self, config):
        super().__init__(config)
        # Custom Step needs custom_class
        if not config.get("custom_class"):
            raise KeyError("Missing custom_class key in config")
        self.custom_module = config["custom_class"]

    def process(self, item):
        """Process item - Custom processing step.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Custom Step")
            item = self.custom_module.process(item)
        except Exception as e:
            self._log.error(
                "Error in custom step (item id:{}) - {}".format(
                    item["id"],
                    e
                )
            )
        return item
