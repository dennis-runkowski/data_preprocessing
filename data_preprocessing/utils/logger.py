""" Setup Logger """

import logging
from datetime import datetime


def setup_logging(name, level="INFO"):
    """
    Method to setup logger

    Args:
        name (str): Name of the logger
        level (str): log level
    Returns:
        obj logger
    """
    logger_name = "{}_{}".format(
        name,
        _create_time_stamp()
    )
    log = logging.getLogger(logger_name)
    log.setLevel(level)
    if level == "DEBUG":
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s '
        )
    else:
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s '
        )
    ch = logging.StreamHandler()
    ch.setLevel(level=level)
    ch.setFormatter(formatter)

    log.addHandler(ch)
    return log


def _create_time_stamp():
    """Create unique id.

    Returns:
        str: Random id as a string
    """
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return str(timestamp)
