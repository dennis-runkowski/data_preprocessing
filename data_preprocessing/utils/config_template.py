"""Templates for config
"""


class Templates:
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
