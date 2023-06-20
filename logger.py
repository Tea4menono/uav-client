import logging

def get_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.propagate = False  # This stops the messages being passed to the root logger
    logger.setLevel(logging.DEBUG)  # Set the minimum logged level to DEBUG

    # Create handlers
    c_handler = logging.StreamHandler()  # Console handler
    f_handler = logging.FileHandler('file.log')  # File handler
    c_handler.setLevel(logging.INFO)  # Set the minimum logged level to INFO for console handler
    f_handler.setLevel(logging.DEBUG)  # Set the minimum logged level to DEBUG for file handler

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

autopilot_logger = get_logger('dronekit')
