"""
Normalize Text - Using the WordNetLemmatizer algorthin
reduce inflectional forms to a common base form.

Example:
    cities -> city
"""
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from data_preprocessing.steps.base import Steps


class Lemmatizer(Steps):
    def __init__(self, config):
        super().__init__(config)
        self.lemmatizer = WordNetLemmatizer()

    def process(self, item):
        """
        Process item - reduce inflectional forms to a common base form.

        Example:
            cities -> city
        Args:
            item (dict): item
        Returns:
            str: text with words converted to a common base form
        """
        try:
            self.log.debug("Lemmatization processing")
            words = word_tokenize(item["data"])
            item_text = ' '.join([self.lemmatizer.lemmatize(w) for w in words])
            return item_text
        except Exception as e:
            self.log.error(
                "Error with lemmatizer on item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]
