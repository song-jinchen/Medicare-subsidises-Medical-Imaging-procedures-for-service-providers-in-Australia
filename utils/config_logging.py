import logging

def config_logging():
    # Configure the root logger
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s - %(message)s',
    filename='mylog.log')

config_logging()
# Example usage
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')