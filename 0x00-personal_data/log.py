"""Logging Module"""
import logging

def logging_finction() -> None:
    """Logging Function"""
    logging.basicConfig(level=logging.WARNING)

    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")


if __name__ == '__main__':
    main()
