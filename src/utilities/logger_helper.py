""" Logger Helper module. """

import logging
import sys
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# A pretty default logging format
DEFAULT_FORMAT = "%(asctime)s|%(levelname)s|%(name)s|%(funcName)s|%(message)s"
DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_TIME_ROTATION = "midnight"
DEFAULT_TIME_INTERVAL = 1


def get_logger(
    log_file: str = "out.log",
    log_level: int = logging.INFO,
    console_level: int = logging.INFO,
    log_format: str = DEFAULT_FORMAT,
    log_time_format: str = DEFAULT_TIME_FORMAT,
    log_time_rotation: str = DEFAULT_TIME_ROTATION,
    log_time_interval: int = DEFAULT_TIME_INTERVAL,    
    log_name: str = None,
) -> logging.Logger:
    """Create a new root logger and sets its formatting and handlers.

    Args:
        log_file (str, optional): Full path to file logger will write to. Defaults to "out.log".
        log_level (int, optional): File logging level. Defaults to logging.INFO.
        console_level (int, optional): Console logging level. Defaults to logging.INFO.
        log_format (str, optional): Log message format. Defaults to DEFAULT_FORMAT.
        log_time_format (str, optional): Log time format. Defaults to DEFAULT_TIME_FORMAT
        log_time_rotation (str, optional): When log time 
        log_time_interval (str, optional): Log time interval
        log_name (str, optional): Log name. Defaults to None.

    Returns:
        new formated root logger
    """

    # Setup new root logger
    new_logger = logging.getLogger(name=log_name)
    new_logger.setLevel(level=log_level)

    # Setup time format
    log_format = logging.Formatter(fmt=log_format, datefmt=log_time_format)

    # Setup file handler - log file will rotate if filesize goes near/equal to maxBytes
    file_handler = RotatingFileHandler(filename=log_file, maxBytes=1000 * 1000)
    file_handler.setLevel(level=log_level)
    file_handler.setFormatter(fmt=log_format)
    new_logger.addHandler(hdlr=file_handler)

    # Setup time handler - log file will rotate at midnight
    time_handler = TimedRotatingFileHandler(
        filename=log_file, when=log_time_rotation, interval=log_time_interval
    )
    time_handler.setLevel(level=log_level)
    time_handler.setFormatter(fmt=log_format)
    new_logger.addHandler(hdlr=time_handler)

    # Setup stream handler - what we see in terminal
    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(level=console_level)
    stream_handler.setFormatter(fmt=log_format)
    new_logger.addHandler(hdlr=stream_handler)

    # Return new logger
    return new_logger
