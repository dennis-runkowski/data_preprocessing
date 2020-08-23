""" Setup Logger """

import logging


def setup_logging(name, level="INFO"):
    """
    Method to setup logger

    Args:
        name (str): Name of the logger
        level (str): log level
    Returns:
        obj logger
    """
    log = logging.getLogger(name)
    log.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )
    ch = logging.StreamHandler()
    ch.setLevel(level=level)
    ch.setFormatter(formatter)

    log.addHandler(ch)
    return log
