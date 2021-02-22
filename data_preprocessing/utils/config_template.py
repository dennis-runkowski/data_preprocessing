"""Templates for config."""


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
        """Pipeline template.
        Returns:
            obj: template for the pipeline
        """
        return {
            "tokenizer": {},
            "data_loader": {},
            "steps": []
        }

    @classmethod
    def data_loader_csv_loader(cls, **kwargs):
        """Data Loader CSV config.

        Args:
            **kwargs: accepts the keyword arguments file_path, columns,
                batch_size and log_level
        Returns:
            obj: csv config object
        """
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
    def data_loader_list_loader(cls, **kwargs):
        """Data Loader List config.

        Args:
            **kwargs: accepts the keyword arguments batch_size and log_level
        Returns:
            obj: list config object
        """
        batch_size = 1000
        log_level = "INFO"

        if kwargs.get("batch_size"):
            batch_size = kwargs["batch_size"]
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "type": "list",
            "batch_size": batch_size,
            "log_level": log_level
        }

    @classmethod
    def data_loader_single_item_loader(cls, **kwargs):
        """Data Loader Single Item config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: single item config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "type": "single_item",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_lowercase(cls, **kwargs):
        """Normalize Text Lowercase config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: lowercase config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "lowercase",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_custom(cls, **kwargs):
        """Normalize Text custom config.

        Args:
            **kwargs: accepts the keyword argument custom_class and log_level
        Returns:
            obj: custom config object
        """
        log_level = "INFO"
        custom_class = ""
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        if kwargs.get("custom_class"):
            log_level = kwargs["custom_class"]
        return {
            "name": "normalize_text",
            "type": "custom_normalize",
            "log_level": log_level,
            "custom_class": custom_class
        }

    @classmethod
    def normalize_text_debugger(cls, **kwargs):
        """Normalize Text debugger config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: debugger config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "debugger_step",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_expand_contractions(cls, **kwargs):
        """Normalize Text expand_contractions config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: expand_contractions config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "expand_contractions",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_lemmatizer(cls, **kwargs):
        """Normalize Text lemmatizer config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: lemmatizer config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "lemmatizer",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_porter_stemmer(cls, **kwargs):
        """Normalize Text porter_stemmer config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: porter_stemmer config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "porter_stemmer",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_snowball_stemmer(cls, **kwargs):
        """Normalize Text snowball_stemmer config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: snowball_stemmer config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "snowball_stemmer",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_remove_digits(cls, **kwargs):
        """Normalize Text remove_digits config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: remove_digits config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "remove_digits",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_remove_html(cls, **kwargs):
        """Normalize Text remove_html config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: remove_html config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "remove_html",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_remove_punctuation(cls, **kwargs):
        """Normalize Text remove_punctuation config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: remove_punctuation config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "remove_punctuation",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_remove_stopwords(cls, **kwargs):
        """Normalize Text remove_stopwords config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: remove_stopwords config object
        """
        log_level = "INFO"
        options = "short_list"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        if kwargs.get("options"):
            options = kwargs["options"]

        return {
            "name": "normalize_text",
            "type": "remove_stopwords",
            "options": options,
            "log_level": log_level
        }

    @classmethod
    def normalize_text_remove_whitespace(cls, **kwargs):
        """Normalize Text remove_whitespace config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: remove_whitespace config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "normalize_text",
            "type": "remove_whitespace",
            "log_level": log_level
        }

    @classmethod
    def normalize_text_remove_urls(cls, **kwargs):
        """Normalize Text remove_urls config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: remove_urls config object
        """
        log_level = "INFO"
        save_urls = "no"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        if kwargs.get("save_urls"):
            save_urls = kwargs["save_urls"]
        return {
            "name": "normalize_text",
            "type": "remove_urls",
            "log_level": log_level,
            "save_urls": save_urls
        }

    @classmethod
    def tokenizer_nltk_word(cls, **kwargs):
        """Tokenizer nltk_word_tokenize config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: nltk_word_tokenize config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "tokenizer",
            "type": "nltk_word_tokenize",
            "log_level": log_level
        }

    @classmethod
    def tokenizer_spaces(cls, **kwargs):
        """Tokenizer spaces config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: spaces config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "tokenizer",
            "type": "spaces",
            "log_level": log_level
        }

    @classmethod
    def tokenizer_nltk_regex(cls, **kwargs):
        """Tokenizer nltk_regex config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: nltk_regex config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "tokenizer",
            "type": "nltk_regex",
            "log_level": log_level
        }

    @classmethod
    def tokenizer_spacy_word_tokenize(cls, **kwargs):
        """Tokenizer spacy_word_tokenize config.

        Args:
            **kwargs: accepts the keyword argument log_level
        Returns:
            obj: spacy_word_tokenize config object
        """
        log_level = "INFO"
        if kwargs.get("log_level"):
            log_level = kwargs["log_level"]
        return {
            "name": "tokenizer",
            "type": "spacy_word_tokenize",
            "log_level": log_level
        }
