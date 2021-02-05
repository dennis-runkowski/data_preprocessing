""" Normalize Text - Debugger step to log the item data.

This class is used to log the data of an item. This step logs the item data.
This is useful when debugging to see the item change as it is moving through
the steps in your pipeline. The config type must be set to `debugger_step`.

Example:
    .. code-block::

        # Example: Using the pipeline
        from data_preprocessing.base import DataPreprocess
        config = {
            "data_loader": {
                "type": "list",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "debugger_step",
                    "log_level": "INFO"
                },
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO"
                },
                {
                    "name": "normalize_text",
                    "type": "debugger_step",
                    "log_level": "INFO"
                }
            ]
        }
        process = DataPreprocess(config)
        data = ["LIST of sentences TO CleAn"]
        for batch in process.process_data(data):
            pass
"""

from data_preprocessing.steps.base import Steps


class DebuggerStep(Steps):
    """Process item - Debugger step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "debugger_step",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """Debugging step to log item text.

        Args:
            item (obj): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self.log.warning("---------------Debugger Step---------------")
            self.log.warning(item["data"])
            self.log.warning("--------------------End--------------------")
        except Exception as e:
            self.log.error(
                "Error debugging (item id:{}) - {}".format(
                    item["id"],
                    e
                )
            )
        return item
