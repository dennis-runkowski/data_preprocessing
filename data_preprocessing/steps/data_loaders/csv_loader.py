""" Process data from a CSV file.

This data loader fetches data from a csv file, formats the data to the item
model and processes through the data preprocessing pipeline. You must include
two columns, one for the id and one for the data. If you want to include
additional columns in the item, you can add the `addition_columns` key with a
list of the column names.

Example:
    .. code-block::

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "csv",
                "file_path": "fake_job_postings.csv",
                "columns": {
                    "id": "job_id",
                    "data": "description",
                    "additional_columns": ["names", "of", "columns"]
                },
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
                "columns": {
                    "id": "job_id",
                    "data": "description",
                    "additional_columns": ["names", "of", "columns"]
                },
                "batch_size": 1000,
                "log_level": "INFO",
                "preserve_original": True # default is False
            }
    """
    def __init__(self, config):
        super().__init__(config)
        self._additional_columns = config["columns"].get("additional_columns")
        if self._additional_columns:
            if not isinstance(self._additional_columns, list):
                raise TypeError("additional_columns must be a list")

    def process(self, *args):
        """Load data from a csv file.

        Transform into a valid item and yield the item.

        Yields:
            obj: Formatted item containing the id and data
        """
        path = self._config["file_path"]
        columns = self._config["columns"]
        column_names = [columns["id"], columns["data"]]
        if self._additional_columns:
            column_names += self._additional_columns
        batch_size = self._config["batch_size"]
        self._log.info(
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
                        self._log.warn("Skipping row - {}".format(index))
                        continue
                    yield self._item_model(item, self._additional_columns)
        except Exception as e:
            self._log.error("Error processing csv file")
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
            if self._additional_columns:
                for c in self._additional_columns:
                    item[c] = row[c]
        except Exception as e:
            self._log.warn("Error processing row in csv file {}".format(e))
            return ""
        return item
