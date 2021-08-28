""" Normalize Text - Expand Contractions step.

This class is used to expand contractions to full length. You must use the
lowercase step prior to this step. This step requires the text to be in
lowercase format. For example, isn't will become is not. The config type must
be set to `expand_contractions`.

Example:
    .. code-block::

        from data_preprocessing.base import DataPreprocess
        config = {
            "data_loader": {
                "type": "single_item",
                "batch_size": 10
            },
            "steps": [
                {
                    "name": "normalize_text",
                    "type": "lowercase",
                    "log_level": "INFO"
                },   
                {
                    "name": "normalize_text",
                    "type": "expand_contractions",
                    "log_level": "INFO"
                }
            ]
        }
        process = DataPreprocess(config)
        data = "I can't go to work."
        data = process.process_item(data)
"""
from data_preprocessing.steps.normalize_text.contractions import CONTRACTIONS
from nltk.tokenize.regexp import regexp_tokenize
from data_preprocessing.steps.base import Steps


class ExpandContractions(Steps):
    """ Expand Contractions step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "expand_contractions",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """Process item - Expand Contractions step.

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Expand Contractions Step")
            text = regexp_tokenize(item["data"], pattern="\s+", gaps=True)  # noqa

            for index, word in enumerate(text):
                if CONTRACTIONS.get(word):
                    text[index] = CONTRACTIONS[word]

            item["data"] = " ".join(text)
        except Exception as e:
            self._log.error(
                "Error debugging (item id:{}) - {}".format(
                    item["id"],
                    e
                )
            )
        return item
