import logging
from logging.handlers import RotatingFileHandler
from config.settings import (
    LOG_DIR,
    LOG_FILE,
    LOG_LEVEL,
    LOG_FORMAT,
    DATE_FORMAT
)

def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger instance.
    """

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger