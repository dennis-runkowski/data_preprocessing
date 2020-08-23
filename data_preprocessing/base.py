""" Base Class to load data """

import json
import csv
import logging
from data_preprocessing.utils.config import validate_config
from data_preprocessing.utils.logger import setup_logging
from data_preprocessing.steps import fetch


class DataPreprocess():
    """Load data and format for processing"""

    def __init__(self, config, log_level="INFO"):
        """
        Pass in the data you want to process

        Args:
            config (obj): Config is a json object
            log_level (str): Set the log level, default is INFO

        Example:
            config = {
                "data": {
                    "data_type": "list",
                    "batch_size": 10
                },
                "steps: {

                }
            }
            process = DataProcess(config)
            testing_data = ["list of sentences to clean"]
            processed_data = []
            for batch in process.run(testing_data):
                processed_data.update(batch)

        """
        self.log = setup_logging(__name__, log_level)
        self.log.info('Validating Config')
        self.config = validate_config(config, log_level)
        self.data_loader = fetch(config["data"])
        self.pipeline_steps = [fetch(s) for s in config.get("steps")]
        self.batch_size = config["data"]["batch_size"]

    def process_data(self, data=None):
        """
        Process data. Data must be a list of dictionaries with the
        keys id and data. If data is not passed in, we assume to load from a
        supported file. The file path needs to be provided in the config.

        Example:
            data = [
                {
                    "id": 1,
                    "data": "this is a string to process"
                },
            ]
        Args:
            data (obj): Dictionary with items to process
        """
        if data:
            self.log.info("Processing {} items".format(len(data)))
        batch = []
        for item in self.data_loader.process(data):
            self.log.debug("Processing item {} - {}".format(
                item["id"],
                item["data"]
            ))
            item = self._process_steps(item)
            self.log.debug("Step completed on item {} - {}".format(
                item["id"],
                item["data"]
            ))
            batch.append(item)
            if len(batch) >= self.batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    def _process_steps(self, item):
        """
        Process data through the defined steps in the config
        Args:
            item (dict): Item to process through the configured steps
        Returns:
            dict: processed item
        """
        for step in self.pipeline_steps:
            item["data"] = step.process(item)

        return item
