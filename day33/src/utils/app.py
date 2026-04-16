import sys
import os

""" add project root to python path
"""

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from conf.logger_cof import setup_logger
""" 
enter point for healthcare application. this module will be responsible for running the main application logic and providing a user interface to interact with the healthcare system. it will utilize the Patient and Doctor classes from the healthcare_app package to manage patient and doctor data, and will also use the logger to log important events and actions within the application.
 """
logger = setup_logger()
def run():
    """
    test logger
    """
    logger.info("Healthcare application started.")
""" handle entey point"""
if __name__ == "__main__":
    run()