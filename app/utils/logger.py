import sys
import logging

from app.settings import CONFIG


def setup_logging(level=None, prefix=None, format=None):
    format = format or '%(asctime)s %(levelname)s {}: %(message)s'.format(prefix)
    level = level or CONFIG.LOG_LEVEL or 'INFO'
    logging.basicConfig(level=level, format=format)


def stdout_handler(level=None):
    handler = logging.StreamHandler(sys.stdout)
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    handler.setFormatter(logging.Formatter(fmt))
    if level:
        handler.setLevel(level)
    return handler


def get_logger(name=None, level=None):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = stdout_handler()
        logger.addHandler(handler)
    return logger

