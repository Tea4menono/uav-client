# logger.py

import logging

def get_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set the minimum logged level to DEBUG

    # Create handlers
    c_handler = logging.StreamHandler()  # Console handler
    c_handler.setLevel(logging.INFO)  # Set the minimum logged level to INFO for console handler

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)

    return logger
