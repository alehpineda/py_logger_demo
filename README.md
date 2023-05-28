# py_logger_demo
Python Logger module demo

### logger_helper.py

Usage example:

```python

# main app

import logging
from utilities import logger_helper
from my_module import my_function

# Setup root logger

LOGGER = logger_helper.get_logger(
    log_file="logs/out.log",  # Log folder needs to exist first else will throw File Not Found Exception
    log_name="main_app"  # Logger name
)

LOGGER.info("Starting")
my_function()
LOGGER.info("Done!")

# sub module

import logging

# In the sub-module just setup the logger with the same name so it will use the root logger's handlers.
LOGGER = logging.getLogger(name="main_app")

def do_something():
    LOGGER.info("Doing something")

```
