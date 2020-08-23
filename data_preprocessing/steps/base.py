""" Base Class for all Steps """

from data_preprocessing.utils.logger import setup_logging


class Steps:
    """ Base Steps Class """
    def __init__(self, config):
        """
        Initialize steps base class
        Args:
            config (obj): config for the step
        """
        self.config = config
        self.log = self._logger()
        self.log.info("Initializing {} step".format(config['type']))

    def _logger(self):
        """
        Helper function to setup logger
        """
        log = setup_logging(
            self.config["type"],
            self.config["log_level"]
        )
        return log
