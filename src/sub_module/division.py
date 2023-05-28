import logging

# In the sub-module just setup the logger with the same name so it will use the root logger's handlers.
LOGGER = logging.getLogger(name="main_app")


def div_error():
    try:
        LOGGER.info("Div by zero")
        LOGGER.debug("Info only for the dev")  # Only appears in debug mode
        return 1 / 0
    except:
        LOGGER.error("Error: Division by zero")  # This shows an Error Logger
        LOGGER.exception(
            "Exception: Division by zero exception with traceback"
        )  # This shows an Error Logger with traceback
