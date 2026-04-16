#configure log format
import logging

""" 
setup logger for healthcare application
 """

def setup_logger():

    """ 
    create and configure logger for healthcare application
     """

    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)

    """
    check if logger already has handlers to avoid duplicate logs in case of multiple imports
    this is important because healthcare_app might be imported in multiple modules and we don't want to add multiple handlers to the same logger
    """
    if logger.hasHandlers():
        return logger
    file_handler = logging.FileHandler('healthcare_app.log')
    logger.setLevel(logging.DEBUG)  

    """ 
    creat formatter to specify log message format and add it to the file handler
     """
     
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger