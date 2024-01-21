"""Logging Module"""
import logging
import datetime

def logging_function() -> None:
    """Logging Function"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H-%M-%S',
        filename='logs.log'
    )
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")


if __name__ == '__main__':
    logging_function()
