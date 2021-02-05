# from data_preprocessing.base import DataPreprocess

# config = {
#     "data_loader": {
#         "type": "list",
#         "batch_size": 10
#     },
#     "steps": [
#         {
#             "name": "normalize_text",
#             "type": "remove_digits",
#             "log_level": "INFO",
#         }
#     ]
# }
# process = DataPreprocess(config)
# data = ["I have 2 dogs and 3 siblings."]
# for batch in process.process_data(data):
#     print(batch)

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
            "log_level": "INFO",
        },
        {
            "name": "normalize_text",
            "type": "remove_whitespace",
            "log_level": "INFO",
        },
        {
            "name": "normalize_text",
            "type": "debugger_step",
            "log_level": "INFO",
        },
    ]
}
process = DataPreprocess(config)
data = [" Remove the whitespace  \n "\
    "       from string of   text "]
for batch in process.process_data(data):
    print(batch)