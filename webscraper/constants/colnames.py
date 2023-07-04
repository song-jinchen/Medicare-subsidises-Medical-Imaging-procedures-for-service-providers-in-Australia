import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


import time
import os

# col_name= 

col_names=['Group','Subgroup','ITEMS', 'NSW','VIC','QLD','SA','WA','TAS','ACT','NT','TOTAL']
I5_columns=['Group','Subgroup','ITEMS','NSW/ACT','VIC/TAS','QLD','SA/NT','WA','TOTAL']

