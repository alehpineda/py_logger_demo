import logging

from sub_module.division import div_error
from utilities import logger_helper

LOGGER = logger_helper.get_logger(
    log_file="logs/out.log",  # Log folder needs to exist first else will throw File Not Found Exception
    log_name="main_app",
    log_level=logging.DEBUG,  # Log File. Changed from DEFAULT INFO.
    console_level=logging.DEBUG,  # Log Console. Changed from DEFAULT INFO.
)


def hello_world():
    LOGGER.info("Starting!")
    print("Hello World!")
    LOGGER.info("Hello World!")
    LOGGER.info("Done!")


if __name__ == "__main__":
    hello_world()
    div_error()  # imported from sub_module
