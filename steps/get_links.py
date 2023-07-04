import logging
from selenium.webdriver.common.by import By
from utils.config_logging import config_logging

config_logging()
def get_links(driver):
    # Find the table
    logging.info("Start to get the subgroup links")
    table = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div/div/table')

    # Find all rows in the table
    logging.info("Find all rows in the table")
    rows = table.find_elements(By.XPATH,'.//tr')

    # Initialize a list to store the data
    table_data = []

    # Loop through each row
    logging.info("Loop through each row")
    for row in rows:
        # Get all columns in each row.
        logging.info("Get all columns in each row")
        columns = row.find_elements(By.XPATH,'.//td | .//th')

        # Get the text from each column
        logging.info("Get the text from each column")
        column_data = [col.text for col in columns]

        # Add the columns to the table_data
        logging.info("Add the columns to the table_data")
        table_data.append(column_data)


    # Get all links in the tbody
    logging.info("Get all links in the tbody")
    links = driver.find_elements(By.CSS_SELECTOR,'tbody a')

    href_values = []

    # Loop through the list of links and extract the href attribute and text from each on
    logging.info("Loop through the list of links and extract the href attribute and text from each")    
    for link in links:
        href_value = link.get_attribute('href')
        # 
        extracted_value = href_value.split("'")[1]
        
        href_values.append(extracted_value) 

    print(href_values)  # Prints the list of href values
    return href_values