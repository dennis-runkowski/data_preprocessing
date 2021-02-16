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
    def get_template_csv(cls):
        """CSV Template"""
        config_template_csv = {
            "data_loader": {
                "type": "csv",
                "file_path": "test.csv",
                "columns": {"id": "id_column", "data": "description"},
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
    def data_loader_csv_loader(cls):
        """Data Loader CSV config."""
        return {
            "type": "csv",
            "file_path": "file_name.csv",
            "columns": {"id": "", "data": ""},
            "batch_size": 1000,
            "log_level": "INFO"
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
