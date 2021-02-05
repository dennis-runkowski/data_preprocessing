""" Normalize Text - Remove urls from test.

This class is used to remove urls from a string of text. If you are using this
step in a pipeline it must come before the step `remove_punctuation`. If you
want to remove urls, but store them as part of the item, you can set the config
option save_urls to `yes`. The config type must be set to `remove_urls`.

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
                    "type": "remove_urls",
                    "save_urls": "yes",
                    "log_level": "INFO"
                }
            ]
        }
        process = DataPreprocess(config)
        testing_data = ["test to remove https://google.com and www.google.com"]
        for batch in process.process_data(testing_data):
            print(batch)
"""
import re
from data_preprocessing.steps.base import Steps


class RemoveUrls(Steps):
    """Remove Urls step class.

    Args:
        config (json): Json object containing the configuration details

    Example:
        .. code-block::

            # config for usage
            config = {
                "name": "normalize_text",
                "type": "remove_urls",
                "save_urls": "yes",  # optional - default is no
                "log_level": "INFO"
            }
    """
    def __init__(self, config):
        super().__init__(config)
        self.regex = r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?'  # noqa

    def process(self, item):
        """Process item - remove urls from the items data

        Args:
            item (dict): item
        Returns:
            dict: Updated item
        """
        try:
            self.log.debug("Remove Urls Step")
            save_urls = self.config.get("save_urls", "no")
            item_data = item["data"]
            if save_urls == "yes":
                urls = []
                regex_iter = re.finditer(
                    self.regex,
                    item_data,
                    flags=re.DOTALL | re.MULTILINE | re.IGNORECASE
                )
                for url in regex_iter:
                    url = url[0]
                    urls.append(url)
                    item_data = item_data.replace(url, "")
                item["tags"]["urls"] = urls
            else:
                item_data = re.sub(
                    self.regex,
                    "",
                    item_data,
                    flags=re.DOTALL | re.MULTILINE | re.IGNORECASE
                )
            item["data"] = item_data
        except Exception as e:
            self.log.error(
                "Error removing urls from item id:{} - {}".format(
                    item["id"],
                    e
                )
            )
        return item
