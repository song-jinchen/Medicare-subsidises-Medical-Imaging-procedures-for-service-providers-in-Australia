import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.config_logging import config_logging
from steps.wait_for_page_load import wait_for_page_load
import time
    
config_logging()




def open_the_page(driver):
    wait_for_page_load(driver)
    
    # Find the dropdown for 'Report on' and select 'Category 5 - Diagnostic Imaging Services'
    logging.info('click on element')
    select_report_on = Select(driver.find_element(By.ID, 'GROUP'))
    select_report_on.select_by_visible_text('Category 5 - Diagnostic Imaging Services')
    assert select_report_on.first_selected_option.text == 'Category 5 - Diagnostic Imaging Services', "Failed to select 'Category 5 - Diagnostic Imaging Services'"
    time.sleep(1)
    logging.info('success')    
        # Find the dropdown for 'Show' and select 'services'
    logging.info('Find the dropdown for "Show" and select "services"') 
    select_show = Select(driver.find_element(By.ID, 'VAR'))
    select_show.select_by_visible_text('services')
    assert select_show.first_selected_option.text == 'services', "Failed to select 'services'"
    time.sleep(1)
        
        # Find the dropdown for 'as' and select 'count'
    logging.info('Find the dropdown for "as" and select "count"') 
    select_as = Select(driver.find_element(By.ID, 'STAT'))
    select_as.select_by_visible_text('count')
    assert select_as.first_selected_option.text == 'count', "Failed to select 'count'"
    time.sleep(1)
        
        # Find the dropdown for 'Report format' and select 'by state (columns)'
    logging.info('Find the dropdown for "Report format" and select "by state (00)"')
    select_report_format = Select(driver.find_element(By.ID, 'RPT_FMT'))
    select_report_format.select_by_visible_text('by state (columns)')
    assert select_report_format.first_selected_option.text == 'by state (columns)', "Failed to select 'by state (columns)'"
    time.sleep(1)
        
        # Find the dropdown for 'Time period' and select 'in financial years'
    logging.info('Finf the dropdown for "Time period" and select "in financial years"') 
    select_time_period = Select(driver.find_element(By.ID, 'PTYPE'))
    select_time_period.select_by_visible_text('in financial years')
    assert select_time_period.first_selected_option.text == 'in financial years', "Failed to select 'in financial years'"
    time.sleep(1)
        
        # Find the dropdown for 'Start date' and select 'July 2022'
    logging.info('Find the dropdown for "Start date" and select "July 202"')
    select_start_date = Select(driver.find_element(By.ID, 'START_DT'))
    select_start_date.select_by_visible_text('July 2022')
    assert select_start_date.first_selected_option.text == 'July 2022', "Failed to select 'July 2022'"
    time.sleep(1)
        
    logging.info('Find the dropdown for "End date" and select The last item')
    select_end_date = Select(driver.find_element(By.ID, 'END_DT'))
    # Get the last option index
    last_option_index = len(select_end_date.options) - 1

    # Select the last option
    select_end_date.select_by_index(last_option_index)
    assert select_end_date.first_selected_option.text == 'April 2023', "Failed to select 'April 2023'"
    time.sleep(1)
        
    logging.info("Click 'create report' button")
    create_report_button = driver.find_element(By.XPATH, '//input[@value="Create Report"]')
    create_report_button.click()

    print("All options successfully selected and report creation started")
    logging.info("All options successfully selected and report creation started")

        
        
    

    





    




