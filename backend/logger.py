"""
=========================================================
CalciSketch Logger
=========================================================

Provides a centralized logger for the application.

All modules should import this logger instead of using print().
"""

import logging
from logging.handlers import RotatingFileHandler

from config import LOG_FILE, LOG_LEVEL


class Logger:
    """
    Singleton logger for the entire application.
    """

    _logger = None

    @classmethod
    def get_logger(cls):
        """
        Returns the configured logger instance.
        """

        if cls._logger is not None:
            return cls._logger

        logger = logging.getLogger("CalciSketch")

        logger.setLevel(getattr(logging, LOG_LEVEL))

        if logger.hasHandlers():
            return logger

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=2 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        cls._logger = logger

        return logger


logger = Logger.get_logger()