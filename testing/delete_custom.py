# from data_preprocessing.steps.normalize_text.custom_normalize import CustomNormalize

config_1 = {
            "name": "normalize_text",
            "type": "custom_normalize",
            "log_level": "INFO",
            "custom_module": "custom_step"
        }
config_3 = {
            "name": "normalize_text",
            "type": "debugger_step",
            "log_level": "INFO",
        }
config_2 = {
            "name": "normalize_text",
            "type": "custom_normalize",
            "log_level": "INFO",
            "custom_module": "custom_step_v2"
        }


# x = CustomNormalize(config_1)
data = {
    "id": 1,
    "data": "LIST of sentences TO CleAn"
}

# d = x.process(data)
# print(d)

# y = CustomNormalize(config_2)
# data = {
#     "id": 1,
#     "data": "LIST of sentences TO CleAn"
# }

# d = y.process(data)
# print(d)

# import importlib
# import inspect
# from data_preprocessing.steps.normalize_text import fetch as normalize_text

# # path = "data_preprocessing.steps.normalize_text.custom_normalize"
# # module = importlib.import_module(
# #             path,
# #             "data_preprocessing"
# #         )
# # test = [
# #     type('ClassHash_1234', (getattr(module, "CustomNormalize"),), {}),
# #     type('ClassHash_1234', (getattr(module, "CustomNormalize"),), {})
# # ]
# # steps = [for i]
# # x = test[0](config_1)
# x = normalize_text(config_1)
# y = normalize_text(config_2)


from data_preprocessing.steps.normalize_text.custom_normalize import CustomNormalize
from data_preprocessing.steps.normalize_text.debugger_step import DebuggerStep
steps = []
for i in [config_1, config_2]:
    steps.append(CustomNormalize(i))
steps.append(DebuggerStep(config_3))
for i in steps:
    print(i.process(data))