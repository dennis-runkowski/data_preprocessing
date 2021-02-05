""" Process data from a CSV file.

This data loader fetches data from a csv file, formats the data to the item 
model and processes through the data preprocessing pipeline. You need to include two
colums, one for the id and one for the data.

Example:
    .. code-block::

        # Example: Stand Alone
        from data_preprocessing.steps.data_loaders import csv_loader

        config = {
            "data_loader": {
                "type": "csv",
                "file_path": "fake_job_postings.csv",
                "columns": {"id": "job_id", "data": "description"},
                "batch_size": 1000,
                "log_level": "INFO"
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO"
                },
            ]
        }

        loader = csv_loader.CsvDataLoader(config["data_loader"])

        for item in loader.process():
            print(item)
            break

        # Example: Using the pipeline
        from data_preprocessing.base import DataPreprocess

        loader = DataPreprocess(config, log_level='INFO')

        for batch in loader.process_data():
            print(batch)
            break

"""
import csv
import pandas as pd
from data_preprocessing.steps.base import Steps


class CsvDataLoader(Steps):
    """CSV Data Loader class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            config = {
                "type": "csv",
                "file_path": "fake_job_postings.csv",
                "columns": {"id": "job_id", "data": "description"},
                "batch_size": 1000,
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, *args):
        """Load data from a csv file.

        Transform into a valid item and yield the item.

        Yields:
            obj: Formatted item containing the id and data
        """
        path = self.config["file_path"]
        columns = self.config["columns"]
        column_names = [columns["id"], columns["data"]]
        batch_size = self.config["batch_size"]
        self.log.info(
            "Loading items from csv file - {}".format(
                path
            )
        )
        try:
            for batch in pd.read_csv(
                    path, usecols=column_names, chunksize=batch_size):

                for index, row in batch.iterrows():
                    item = self._build_item(row, columns)
                    if not item:
                        self.log.warn("Skipping row - {}".format(index))
                        continue
                    yield self.item_model(item)
        except Exception as e:
            self.log.error("Error processing csv file")
            raise e

    def _build_item(self, row, columns):
        """Internal method to build the item in the right
        format.

        Example:
            item = {
                "id": 1,
                "data": "data to process"
            }
        Args:
            row (obj): Pandas df row
            columns (dict): dict containing the columns for id and data
        Returns:
            dict: item
        """
        try:
            item = {
                "id": row[columns["id"]],
                "data": row[columns["data"]]
            }
        except Exception as e:
            self.log.warn("Error processing row in csv file {}".format(e))
            return ""
        return item
