""" Base Class to load data """

import json
import csv
import logging
import queue
from time import process_time
import multiprocessing as mp
from data_preprocessing.utils.config import validate_config
from data_preprocessing.utils.logger import setup_logging
from data_preprocessing.steps import fetch


class DataPreprocess():
    """Load data and format for processing"""

    def __init__(self, config, log_level="INFO"):
        """Initialize the DataPreprocessing class.

        Args:
            config (obj): Config is a json object
            log_level (str): Set the log level, default is INFO

            Example Usage:
                config = {
                    "data_loader": {
                        "type": "list",
                        "batch_size": 10
                    },
                    "steps: [
                        {
                            "name": "normalize_text",
                            "type": "lowercase",
                            "log_level": "INFO"
                        }
                    ]
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
        self.data_loader = fetch(config["data_loader"])
        self.pipeline_steps = [fetch(s) for s in config.get("steps")]
        self.batch_size = config["data_loader"]["batch_size"]

        # Start time
        self.start_time = process_time()
        self.items_processed = 0

    def process_data(self, data=None):
        """Process data through the defined pipeline.

        # TODO - fix list loader to be a true list
        The Data arg is only used when loading in memory data like a list.

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
            self.items_processed += 1
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

    def multiprocess_data(self, data=None):
        """Process data through the defined pipeline.

        # TODO - fix list loader to be a true list
        The Data arg is only used when loading in memory data like a list.

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
        processes = []
        self.queue = mp.JoinableQueue()
        self.kafka_queue = mp.Queue()

        for i in range(4):
            worker_process = mp.Process(
                target=self._worker,
                args=(self.queue, self.kafka_queue),
                daemon=True,
                name='worker_process_{}'.format(i)
            )
            worker_process.start()
            processes.append(worker_process)
        self.log.info([x.name for x in processes])
        if data:
            self.log.info("Processing {} items".format(len(data)))
        for item in self.data_loader.process(data):
            self.items_processed += 1
            self.queue.put(item)

        self.queue.join()

        for item in range(0, self.kafka_queue.qsize()):
            yield self.kafka_queue.get()

    def disconnect(self):
        """Method to call to get the stats of processing."""
        end_time = process_time()
        self.log.info("Processing took {a} seconds.".format(
            a=end_time - self.start_time
        ))
        self.log.info("{} items were processed.".format(self.items_processed))

    def _process_steps(self, item):
        """Process data through the defined steps in the config.

        Args:
            item (dict): Item to process through the configured steps
        Returns:
            dict: processed item
        """
        for step in self.pipeline_steps:
            item["data"] = step.process(item)

        return item

    def _worker(self, queue, kafka_queue):
        while True:
            msg = queue.get()
            msg = self._process_steps(msg)
            kafka_queue.put(msg)
            queue.task_done()
