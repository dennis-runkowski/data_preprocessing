"""Templates for config
"""


class PreBuiltTemplates:
    @classmethod
    def get_template(cls):
        """General Template."""
        config_template = {
            "data_loader": {
                "type": "",
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO"
                },
            ]
        }
        return config_template

    @classmethod
    def get_template_csv(cls, **kwargs):
        """CSV Template"""
        file_path = ""
        columns = {"id": "id", "data": "description"}
        batch_size = 1000
        log_level = "INFO"

        if kwargs.get("file_path"):
            file_path = kwargs["file_path"]
        if kwargs.get("columns"):
            columns = kwargs["columns"]
        if kwargs.get("batch_size"):
            batch_size = kwargs["batch_size"]
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]

        config_template_csv = {
            "data_loader": {
                "type": "csv",
                "file_path": file_path,
                "columns": columns,
                "batch_size": batch_size,
                "log_level": log_level
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO"
                },
            ]
        }
        return config_template_csv

    @classmethod
    def get_template_single(cls):
        """Template for single item."""
        config_template = {
            "data_loader": {
                "type": "single_item",
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO"
                },
            ]
        }
        return config_template


class ConfigTemplates:
    @classmethod
    def pipeline(cls):
        """Pipeline template."""
        return {
            "tokenizer": {},
            "data_loader": {},
            "steps": []
        }

    @classmethod
    def data_loader_csv_loader(cls, **kwargs):
        """Data Loader CSV config."""
        file_path = ""
        columns = {"id": "id", "data": "description"}
        batch_size = 1000
        log_level = "INFO"

        if kwargs.get("file_path"):
            file_path = kwargs["file_path"]
        if kwargs.get("columns"):
            columns = kwargs["columns"]
        if kwargs.get("batch_size"):
            batch_size = kwargs["batch_size"]
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]

        return {
            "type": "csv",
            "file_path": file_path,
            "columns": columns,
            "batch_size": batch_size,
            "log_level": log_level
        }

    @classmethod
    def data_loader_list_loader(cls):
        """Data Loader List config."""
        return {
            "type": "list",
            "batch_size": 1000,
            "log_level": "INFO"
        }

    @classmethod
    def data_loader_single_item_loader(cls):
        """Data Loader Single Item config."""
        return {
            "type": "single_item",
            "log_level": "INFO"
        }

    @classmethod
    def normalize_text_lowercase(cls):
        """Normalize Text Lowercase config."""
        return {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": "INFO"
        }
