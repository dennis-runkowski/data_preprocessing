"""
Normalize Text - Using the PorterStemmer algorthin stem words
into their root word.

Example:
    visiting -> visit
"""
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from data_preprocessing.steps.base import Steps


class Stemmer(Steps):
    def __init__(self, config):
        super().__init__(config)
        self.porter_stemmer = PorterStemmer()

    def process(self, item):
        """
        Process item - stem words into their root word using the
        PorterStemmer algorthim.

        Example:
            visiting -> visit
        Args:
            item (dict): item
        Returns:
            str: text with words converted to their root form
        """
        try:
            self.log.debug("Stemming words")
            words = word_tokenize(item["data"])
            item_text = ' '.join([self.porter_stemmer.stem(w) for w in words])
            return item_text
        except Exception as e:
            self.log.error(
                "Error stemming from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]
