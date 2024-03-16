import logging

# Configure the logging module
logging.basicConfig(level=logging.DEBUG)

# Messages with the "logger" object
logger = logging.getLogger("my_app")

logger.debug("A debug message.")
logger.info("An informational message.")
logger.warning("A warning message.")
logger.error("An error message.")
logger.critical("A critical message.")