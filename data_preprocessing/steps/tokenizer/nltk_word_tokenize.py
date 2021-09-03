"""Tokenize Text - split text into tokens using nltk `word_tokenize`

Example:
    .. code-block::

        from data_preprocessing import DataPreprocess

        config = {
            "data_loader": {
                "type": "single_item",
                "batch_size": 10
            },
            "tokenizer": [
                {
                    "name": "tokenizer",
                    "type": "nltk_word_tokenize",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = "I am going to the mall."
        data = process.process_item(data):
        print(data)
"""
from nltk.tokenize import word_tokenize
from data_preprocessing.steps.base import Steps


class TokenizeNLTKWord(Steps):
    """NLTK Word Tokenizer step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "tokenizer",
                "type": "nltk_word_tokenize",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """Process Item - Tokenize text into tokens.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("NLTK Word Tokenize Step")
            item["data"] = word_tokenize(item["data"])
        except Exception as e:
            self._log.error(
                "Error in NLTK Word Tokenize from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
