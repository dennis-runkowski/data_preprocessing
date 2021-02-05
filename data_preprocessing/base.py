""" Base Class to process data through the pipeline.

The DataPreprocess class is used to process your data through a list of steps. 
You must pass in a config object that contains a valid data loader and a list
of processing steps. Each record is converted into our item mode, which is a
dictionary with an unique id and the raw data.

Example:
    .. code-block::

        from data_preprocessing.base import DataPreprocess
        config = {
            "data_loader": {
                "type": "list",
                "batch_size": 10
            },
            "steps": [{
                "name": "normalize_text",
                "type": "lowercase",
                "log_level": "INFO"
            }]
        }
        process = DataProcess(config)
        data = ["List Of Sentences To Clean"]
        processed_data = []
        for batch in process.process_data(data):
            processed_data.update(batch)
"""

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
    """Load data and process through pipeline.

    Args:
        config (obj): Config is a json object
        log_level (str): Set the log level, default is INFO
    """

    def __init__(self, config, log_level="INFO"):
        """Initialize the DataPreprocessing class."""
        self.log = setup_logging(__name__, log_level)
        self.log.info('Validating Config')
        self.config = validate_config(config, log_level)
        self.data_loader = fetch(config["data_loader"])
        self.pipeline_steps = [fetch(i) for i in config.get("steps")]
        self.batch_size = config["data_loader"]["batch_size"]

        # Start time
        self.start_time = process_time()
        self.items_processed = 0

    def process_data(self, data=None):
        """Generator to process data through the defined pipeline.

        The Data arg is only used when loading in memory data like a list. The
        processed data will be streamed in batches. The size is defined in the
        data loader configuration.

        Args:
            data (obj): Dictionary with items to process
        Yields:
            obj: List of processed items

        Example:
            .. code-block::

                from data_preprocessing.base import DataPreprocess
                config = {
                    "data_loader": {
                        "type": "list",
                        "batch_size": 10
                    },
                    "steps": [{
                        "name": "normalize_text",
                        "type": "lowercase",
                        "log_level": "INFO"
                    }]
                }
                process = DataProcess(config)
                data = ["List Of Sentences To Clean"]
                processed_data = []
                for batch in process.process_data(data):
                    processed_data.update(batch)
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

    def multiprocess_data(self, data=None, workers=1):
        """Generator that uses multiprocessing to process data.

        The Data arg is only used when loading in memory data like a list. The
        processed data will be streamed in batches. The size is defined in the
        data loader configuration.

        Args:
            data (obj): Dictionary with items to process
            workers (int): Number of workers for processing
        Yields:
            dict: Process Item

        Example:
            .. code-block::

                from data_preprocessing.base import DataPreprocess
                config = {
                    "data_loader": {
                        "type": "list",
                        "batch_size": 10
                    },
                    "steps": [{
                        "name": "normalize_text",
                        "type": "lowercase",
                        "log_level": "INFO"
                    }]
                }
                process = DataProcess(config)
                data = ["List Of Sentences To Clean"]
                processed_data = []
                for batch in process.multiprocess_data(data, workers=4):
                    processed_data.update(batch)
        """
        processes = []
        self.queue = mp.JoinableQueue()
        self.kafka_queue = mp.Queue()

        for i in range(workers):
            worker_process = mp.Process(
                target=self._worker,
                args=(self.queue, self.kafka_queue),
                daemon=True,
                name='data_preprocess_worker_{}'.format(i)
            )
            worker_process.start()
            processes.append(worker_process)
        self.log.info("Setting up workers - {}".format(
                ", ".join([x.name for x in processes])
            )
        )
        if data:
            self.log.info("Processing {} items".format(len(data)))
        for item in self.data_loader.process(data):
            self.items_processed += 1
            self.queue.put(item)

        self.queue.join()

        for item in range(0, self.kafka_queue.qsize()):
            yield self.kafka_queue.get()

    def disconnect(self):
        """Method to get the stats of processing.

        This should be called after the data is processed.

        Example:
            .. code-block::

                from data_preprocessing.base import DataPreprocess
                config = {
                    "data_loader": {
                        "type": "list",
                        "batch_size": 10
                    },
                    "steps": [{
                        "name": "normalize_text",
                        "type": "lowercase",
                        "log_level": "INFO"
                    }]
                }
                process = DataProcess(config)
                data = ["List Of Sentences To Clean"]
                for batch in process.process_data(data):
                    pass
                process.disconnect()
        """
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
            item = step.process(item)

        return item

    def _worker(self, queue, kafka_queue):
        while True:
            msg = queue.get()
            msg = self._process_steps(msg)
            kafka_queue.put(msg)
            queue.task_done()
