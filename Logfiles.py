import logging
# import logging.config
from gitignoreme.agent_constants import get_log_file_path 


def get_logger(module_name):
    logger = logging.getLogger(module_name)
    # logger.setLevel(logging.INFO)
    # from https://google.github.io/adk-docs/observability/logging/#how-to-configure-logging

    formatter = logging.Formatter('%(asctime)s:%(levelname)s : %(name)s : %(message)s')
    file_handler = logging.FileHandler(
        filename=get_log_file_path(),
        mode='a', ## append mode  
    )

    file_handler.setFormatter(formatter)

    if (logger.hasHandlers()):
        logger.handlers.clear()
    
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    
    return logger

# get_logger('Logfiles')