"""Normalize Text - Stem words using the PorterStemmer algorithm

Stem words into their root form. For Example visting becomes visit. The config
type must be set to `porter_stemmer`.

Example:
    .. code-block::

        from data_preprocessing.base import DataPreprocess

        config = {
            "data_loader": {
                "type": "list",
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
        data = ["I am going to the mall."]
        for batch in process.process_data(data):
            print(batch)
"""
from nltk.stem import PorterStemmer
from nltk.tokenize.regexp import regexp_tokenize
from data_preprocessing.steps.base import Steps


class Stemmer(Steps):
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
        self.porter_stemmer = PorterStemmer()

    def process(self, item):
        """Process Item - Stem words into their root word.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self.log.debug("Porter Stemmer Step")
            text = regexp_tokenize(item["data"], pattern="\s+", gaps=True)
            text = " ".join([self.porter_stemmer.stem(w) for w in text])
            item["data"] = text
        except Exception as e:
            self.log.error(
                "Error stemming from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
