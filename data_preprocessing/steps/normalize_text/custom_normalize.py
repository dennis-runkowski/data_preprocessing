""" Normalize Text - Custom normalize step.

This class is used to add a custom step to the pipeline. In order to use this
you must create a module with a function called process that takes one argument
for the data. The module must be in the same location you are running the
process from. You must return the item in order for it to finish through the
remainder of the pipeline. In your config you must add the key `custom_path`
that contains the custom module location. The default module is called
custom_step. The config type must be set to `custom_normalize`

Example:
    .. code-block::

        # Saved in a file called custom_module.py (in the same location)
        def process(item):
            item['data'] = item['data'].upper()
            return item

        from data_preprocessing.base import DataPreprocess

        config = {
            "data_loader": {
                "type": "single_item",
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "debugger_step",
                    "log_level": "INFO"
                },
                {
                    "name": "normalize_text",
                    "type": "custom_normalize",
                    "log_level": "INFO",
                    "custom_module": "custom_module"
                },
                {
                    "name": "normalize_text",
                    "type": "debugger_step",
                    "log_level": "INFO"
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
                "custom_module": "custom_module"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        path = config["custom_module"]
        self.custom_module = importlib.import_module(
            path
        )

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
                "Error debugging (item id:{}) - {}".format(
                    item["id"],
                    e
                )
            )
        return item
