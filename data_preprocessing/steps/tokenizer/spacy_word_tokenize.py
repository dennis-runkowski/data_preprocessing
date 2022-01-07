"""Tokenize Text - split text into tokens using spacy default `Tokenizer`

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
                    "type": "spacy_word_tokenize",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = "I am going to the mall."
        data = process.process_item(data):
        print(data)
"""
import spacy
from data_preprocessing.steps.base import Steps


class TokenizeSpacyWord(Steps):
    """NLTK Regex Tokenizer step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "tokenizer",
                "type": "spacy_word_tokenize",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        self._nlp = spacy.load("en_core_web_lg")

    def process(self, item):
        """Process Item - Tokenize text into tokens.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Spacy Tokenize Step")
            doc = self._nlp(item["data"])
            item["data"] = [token.text for token in doc]
        except Exception as e:
            self._log.error(
                "Error in Spacy Tokenize from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
