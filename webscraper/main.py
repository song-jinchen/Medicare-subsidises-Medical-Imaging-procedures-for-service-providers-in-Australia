from steps.open_page import open_the_page
from steps.extract_data import extract_data
# from excractData import 
import logging
from utils.config_logging import config_logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
config_logging()


if __name__ == "__main__":
    
    # Set up the webdriver
    logging.info("web driver configing")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")  # Adjust log level to suppress messages
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # # Go to the website
    driver.get('http://medicarestatistics.humanservices.gov.au/statistics/mbs_group.jsp')
    
    with open('mylog.log','w'):
        pass
    logging.info("program start")
    open_the_page(driver)
    extract_data(driver)