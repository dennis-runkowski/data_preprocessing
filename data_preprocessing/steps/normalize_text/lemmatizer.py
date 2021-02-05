"""Normalize Text - Lemmatizer Step.

Using the WordNetLemmatizer algorthin reduce inflectional forms to a common
base form. For example cities becomes city. The config type must be set to
`lemmatizer`.

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
                    "type": "lemmatizer",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = ["How many cities are in the USA."]
        for batch in process.process_data(data):
            print(batch)
"""
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.regexp import regexp_tokenize
from data_preprocessing.steps.base import Steps


class Lemmatizer(Steps):
    """Lemmatizer step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "lemmatizer",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        self.lemmatizer = WordNetLemmatizer()

    def process(self, item):
        """Process item - Reduce inflectional forms to a common base form.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self.log.debug("Lemmatizer Step")
            text = regexp_tokenize(item["data"], pattern="\s+", gaps=True)
            text = " ".join([self.lemmatizer.lemmatize(w) for w in text])
            item["data"] = text
        except Exception as e:
            self.log.error(
                "Error with lemmatizer on item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
