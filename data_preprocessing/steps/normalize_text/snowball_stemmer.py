"""Normalize Text - Stem words using the Snowball Stemmer algorithm

From NLTK: The algorithms have been developed by Martin Porter.
These stemmers are called Snowball, because Porter created
a programming language with this name for creating
new stemming algorithms. There is more information available
at http://snowball.tartarus.org/

Stem words into their root form. For Example visting becomes visit. The config
type must be set to `porter_stemmer`.

Example:
    .. code-block::

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "list",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "snowball_stemmer",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = ["I am going to the mall."]
        for batch in process.process_data(data):
            print(batch)
"""
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize.regexp import regexp_tokenize
from data_preprocessing.steps.base import Steps


class NLTKSnowballStemmer(Steps):
    """Snowball Stemmer step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "porter_stemmer",
                "options": "english", # optional - english by default
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        self._validate_config()
        language = self._config["options"]
        self._snowball_stemmer = SnowballStemmer(language=language)

    def process(self, item):
        """Process Item - Stem words into their root word.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Snowball Stemmer Step")
            item = self._tokenizer.process(item)
            text = " ".join(
                [self._snowball_stemmer.stem(w) for w in item["data"]]
            )
            item["data"] = text
        except Exception as e:
            self._log.error(
                "Error stemming from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item

    def _validate_config(self):
        """Validate Config"""
        # Snowball Stemmer can accept options - default is english
        options = self._config.get("options", "english")
        supported_lang = [
            "arabic",
            "danish",
            "dutch",
            "english",
            "finnish",
            "french",
            "german",
            "hungarian",
            "italian",
            "norwegian",
            "porter",
            "portuguese",
            "romanian",
            "russian",
            "spanish",
            "swedish"
        ]
        if options not in supported_lang:
            raise ValueError(
                "This is not a supported language, please use choose "
                "from the supported languages: {}".format(
                    supported_lang
                )
            )
        self._config["options"] = options
