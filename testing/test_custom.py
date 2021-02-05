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
            "type": "custom_normalize",
            "log_level": "INFO",
            "custom_module": "custom_step"
        },
        {
            "name": "normalize_text",
            "type": "debugger_step",
            "log_level": "INFO"
        },
        {
            "name": "normalize_text",
            "type": "custom_normalize",
            "log_level": "DEBUG",
            "custom_module": "custom_step_v2"
        },
        {
            "name": "normalize_text",
            "type": "debugger_step",
            "log_level": "INFO"
        },
    ]
}


process = DataPreprocess(config)
data = ["LIST of sentences TO CleAn"]
for batch in process.process_data(data):
    pass
