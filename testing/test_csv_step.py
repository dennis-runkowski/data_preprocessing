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
