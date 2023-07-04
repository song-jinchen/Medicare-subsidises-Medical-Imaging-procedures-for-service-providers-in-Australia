import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.colnames import col_names,I5_columns
from utils.config_logging import config_logging
from steps.get_links import get_links
import time
import os

import pandas as pd
from steps.handle_exceptions import handle_exceptions


config_logging()


def save_to_csv(driver,index,value,column_names,output_file):
    # Execute JavaScript code that invokes the function present in the href attribute
    logging.info("Execute JavaScript code that invokes the function present in the href attribute")
    driver.execute_script(f"d('{value}')")

    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-floater"]/div[3]/div/div/table')))

    # Extract group and subgroup information
    logging.info("Extract group and subgroup information")
    group_info = driver.find_element(By.XPATH, '//h1').text
    group = group_info.split("Group:")[1].split(",")[0].strip()
    subgroup = group_info.split("Subgroup:")[1].split('"')[0].strip()

    #set header:
    logging.info("set header:")
    rows_elements = table.find_elements(By.XPATH, './/tbody/tr')

    # Prepare a list to hold all rows
    logging.info("Prepare a list to hold all rows")
    rows = []

    # For each pair of rows, extract all the th and td elements
    logging.info("For each pair of rows, extract all the th and td elements")
    for i in range(0, len(rows_elements)-1):
        th_index=0
        if i==1:
            continue
        if i==0:
            th_index=1
        else:
            th_index=i
        # Extract the td elements from the first row of the pair
        logging.info("Extract the td elements from the first row of the pair")
        td_elements = rows_elements[i].find_elements(By.XPATH, './/td')
        td_values = [td.text for td in td_elements]

        # Check if the second row exists
        logging.info("Check if the second row exists")
        if i+1 < len(rows_elements):
            # Extract the th elements from the second row of the pair
            logging.info("Extract the th elements from the second row of the pair")
            th_elements = rows_elements[th_index].find_elements(By.XPATH, './/th/a')
            th_values = [th.text for th in th_elements]
        else:
            th_values = ['Total']
            
        new_td_values = handle_exceptions(group,subgroup,value,td_values)
        
                    
        # Create a new row with group, subgroup, th values from second row and td values from first row
        logging.info("Create a new row with group, subgroup, th values from second row")
        new_row = [group, subgroup] + th_values + new_td_values

        # Add this new row to the rows list
        logging.info("Add this new row to the rows list")
        rows.append(new_row)

    # Convert to DataFrame 
    logging.info("Convert to DataFrame")
    df = pd.DataFrame(rows, columns=column_names)

    # Convert to DataFrame 
    # df = pd.DataFrame(rows, columns=column_names)
    # df.loc[len(df)] = list
    logging.info(df)
    print(df)

    logging.info('write into the csv')
    if not os.path.isfile(output_file) or index == 0:
        df.to_csv(output_file, mode='a', index=False)
    else:
        df.to_csv(output_file, mode='a', index=False, header=False)