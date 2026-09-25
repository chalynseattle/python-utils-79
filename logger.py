import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """Initializes a rotating file logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Ensure directory exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotating handler: 5MB per file, max 3 backups
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

if __name__ == '__main__':
    # Usage example for the project
    app_logger = setup_logger('app_logger', 'logs/app.log')
    app_logger.info('Logger initialized successfully')