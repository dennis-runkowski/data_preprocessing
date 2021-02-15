""" Normalize Text - Remove HTML 

Remove all the html from the data in an item. If you use this step it must run
before the steps `remove_punctuation`, `porter_stemmer`, `lemmatizer`. The
config type must be set to `remove_html`.

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
                    "type": "remove_html",
                    "log_level": "INFO",
                }
            ]
        }
        process = DataPreprocess(config)
        data = ['<h1>Remove Html</h1><p class="test">This is a test.</p>']
        for batch in process.process_data(data):
            print(batch)
"""
from html.parser import HTMLParser
from data_preprocessing.steps.base import Steps


class _RemoveHtmlParser(HTMLParser):
    def __init__(self):
        self.reset()
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return "".join(self.fed).strip()


class RemoveHtml(Steps):
    """Remove Html step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "remove_html",
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """Process item - remove html from text

        Args:
            item (dict): item
        Returns:
            dict: Returns the updated item
        """
        try:
            self._log.debug("Remove HTML Step")
            item["data"] = self._strip_html(item["data"])
        except Exception as e:
            self._log.error(
                "Error removing html from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item

    def _strip_html(self, html):
        """ Strip html using the _RemoveHtmlParser class.

        Args:
            html (str): html text
        Returns:
            str: text with no html
        """
        s = _RemoveHtmlParser()
        s.feed(html)
        return s.get_data()
