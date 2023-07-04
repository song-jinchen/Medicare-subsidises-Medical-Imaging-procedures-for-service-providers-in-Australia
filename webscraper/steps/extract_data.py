import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.colnames import col_names,I5_columns
from utils.config_logging import config_logging
from steps.get_links import get_links
from steps.save_to_csv import save_to_csv
import time
import os

import pandas as pd
from utils.remove_file import remove_file


config_logging()
def extract_data(driver):
    
    ##clean up csv
    logging.info("clean up csv")
    remove_file('output.csv')
    remove_file('output_I5.csv')

    time.sleep(5)
    

    href_values = get_links(driver)
    
    logging.info("Start Processing data in the subgroup pages")
    for index, value in enumerate(href_values):
        
        if not value.startswith('I05'):
            save_to_csv(driver,index,value,col_names,"output.csv")
        else:
            save_to_csv(driver,index,value,I5_columns,'output_I5.csv')

            
        # Switch back to the main page
        logging.info("Switch back to the main page")
        driver.back()

        # Wait for the main page to load
        logging.info("Wait for the main page to load")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody a')))