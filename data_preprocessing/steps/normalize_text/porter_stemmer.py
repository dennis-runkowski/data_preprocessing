"""Normalize Text - Stem words using the PorterStemmer algorithm

Stem words into their root form. For Example visting becomes visit. The config
type must be set to `porter_stemmer`.

Example:
    .. code-block::

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "single_item",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "porter_stemmer",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = "sentences TO CleAn!"
        data = process.process_item(data)
"""
from nltk.stem import PorterStemmer
from nltk.tokenize.regexp import regexp_tokenize
from data_preprocessing.steps.base import Steps


class NLTKPorterStemmer(Steps):
    """Porter Stemmer step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "porter_stemmer",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        self._porter_stemmer = PorterStemmer()

    def process(self, item):
        """Process Item - Stem words into their root word.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Porter Stemmer Step")
            item = self._tokenizer.process(item)
            item["data"] = " ".join(
                [self._porter_stemmer.stem(w) for w in item["data"]]
            )
        except Exception as e:
            self._log.error(
                "Error stemming from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
