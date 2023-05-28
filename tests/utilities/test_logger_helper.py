""" Test module for logger helper """

import os

from utilities.logger_helper import get_logger


def test_create_log():
    src_path = os.path.dirname(os.path.realpath(__file__))
    test_log_file = f"{src_path}/test_out.log"
    
    # Make sure log file doesn't exist for dev env.
    assert os.path.isfile(test_log_file) is False
    
    # Create log
    logger = get_logger(log_file=test_log_file)
    
    # Write log
    logger.info('Hello World from test!')
    
    # Assert log was created
    assert os.path.isfile(test_log_file)
    
    # Remove log file from local env
    os.remove(test_log_file)
    assert os.path.isfile(test_log_file) is False
