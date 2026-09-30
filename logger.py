import logging
import sys
from typing import Optional, Union

def configure_logger(
    name: str,
    level: Union[int, str] = logging.INFO,
    log_file: Optional[str] = None,
    console: bool = True
) -> logging.Logger:
    """
    Configure and return a custom logger with console and file options.

    Args:
        name: Name of the logger.
        level: Logging level as an integer or string (e.g. "INFO", logging.DEBUG).
        log_file: Optional file path to write logs to.
        console: Whether to log messages to the console (sys.stdout).

    Returns:
        A configured Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handlers to prevent duplicate messages
    if logger.hasHandlers():
        logger.handlers.clear()

    log_format = "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"
    formatter = logging.Formatter(log_format)

    if console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger