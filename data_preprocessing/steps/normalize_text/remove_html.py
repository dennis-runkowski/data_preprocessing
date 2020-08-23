""" Normalize Text - Remove HTML """
from html.parser import HTMLParser
from data_preprocessing.steps.base import Steps


class HtmlStrip(HTMLParser):
    def __init__(self):
        self.reset()
        self.convert_charrefs = True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return "".join(self.fed).strip()


class RemoveHtml(Steps):
    def __init__(self, config):
        super().__init__(config)

    def process(self, item):
        """
        Process item - remove html from text
        Args:
            item (dict): item
        Returns:
            str: text with no html tags
        """
        try:
            self.log.debug("Removing html")
            item_text = self.strip_html(item["data"])
            return item_text
        except Exception as e:
            self.log.error(
                "Error removing html from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item["data"]

    def strip_html(self, html):
        """
        Strip html using the HtmlStrip class
        Args:
            html (str): html text
        Returns:
            str: text with no html
        """
        s = HtmlStrip()
        s.feed(html)
        return s.get_data()
