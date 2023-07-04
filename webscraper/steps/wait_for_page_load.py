import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_logging import config_logging

config_logging()

def wait_for_page_load(driver):
    logging.info("get the start page to medicare australia")
    try:
        logging.info('Wait until the element with the id appName is found')
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "appName"))
        )
            # Check if the element's text is 'Medicare Statistics'
        if element.text == "Medicare Statistics":
            logging.info('Element found')
            print("Element found")
        else:
            logging.warning('Element text is not "Medicare Statistics"')
            print("Element text is not 'Medicare Statistics'")
    except:
        print("Element not found")
        logging.warning("Element not found")