from data_preprocessing.base import DataPreprocess

config = {
    "data_loader": {
        "type": "csv",
        "file_path": "./fake_job_postings.csv",
        "columns": {"id": "job_id", "data": "description"},
        "batch_size": 100,
        "log_level": "DEBUG"
    },
    "steps": [
        {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
    ]
}
processer = DataPreprocess(config)
testing_data = ["this is a test", "list loader testing"]    
for batch in processer.multiprocess_data(workers=4):
    pass
    # print(batch[0]['id'])

processer.disconnect()