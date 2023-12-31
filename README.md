# Medicare-subsidises-Medical-Imaging-procedures-for-service-providers-in-Australia
using selenium scrap the data from Medicare Australia which can extract data for category 5 and the financial year from 2022/07-2023/04（2023/04-2023/06 not published)

## Project Description

This project is a Python-based web scraper designed to extract information on medical procedures from a website. The script navigates through multiple pages, interacts with JavaScript functions, and extracts table data. The extracted data includes details about medical procedure groups, subgroups, and specific information like procedure counts per geographical region. Also, the code can be re-executed to collect data for future months that aren't yet published

## Packages Used 

- **Selenium:** For automating web browser interaction from Python.
- **Pandas:** For data manipulation and analysis.
- **os and sys:** Basic Python packages used for interacting with the system.

## How to Setup the Project

1. **Install the required packages:**

    Open your terminal and execute the following commands:

    ```shell
    pip install selenium
    pip install webdriver_manager
    pip install pandas
    ```

    These commands will install Selenium, WebDriver Manager, and pandas packages that are required for this project.
   
2. **Download the ChromeDriver:**

    Download the correct version of [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads) and place it in the same directory as your script.

3. **Run the code:**

    After completing the above steps, you can run the project. Use the following command to run the script:

    ```shell
    python -u main.py
    ```

Please note: Depending on your Python setup, you may need to use `pip3` instead of `pip` for the installation commands. And you may need to use `python3` instead of `python` for the command to run the script.




### Approach and Solution

This project involved scraping a complex, dynamic website with a varying number of table columns across different pages. Our approach consisted of using Python, a powerful programming language, and Selenium, a robust tool for automating browsers. 

The key steps in our solution were:

1. Navigating the website by executing JavaScript functions with Selenium WebDriver.
2. Extracting table data dynamically, accounting for the variability in the number of columns.
3. Cleaning and formatting the extracted data before writing it to a CSV file.

Despite encountering various challenges, we were able to scrape the required data and achieve the project objectives successfully.

## Challenges Faced

The major challenges during the project included dealing with JavaScript-heavy navigation, long loading times for certain pages, dynamic data structure, and substantial data cleaning. These challenges were overcome by effectively using the features and functions provided by Selenium, like `WebDriverWait` for handling loading times, executing JavaScript code for navigation, and applying conditional statements for handling the dynamic data structure.

1. **Handling JavaScript Functions:** The website navigation heavily relied on JavaScript functions. Selenium WebDriver was used to execute JavaScript code and navigate through the site.

2. **Loading Time:** Some pages took longer to load than others, and elements were not immediately available. The `WebDriverWait` function from Selenium was used to solve this issue.

3. **Dynamic Data Structure:** The structure of the data on the website was not consistent. Some pages had more columns than others, and the first two rows in the table body didn't have corresponding data and item names. This was handled by using conditional statements to adjust the data extraction process based on the structure of the data.

4. **Data Cleaning:** The extracted data required substantial cleaning before it could be used. This included handling missing values, adjusting data formats, and inserting additional values for certain records.
5. **Non-standard file format:** Even though there is a 'download excel' option on the website, the downloaded file is in HTML format rather than a standard Excel format. This means it could not be directly converted into CSV. To overcome this, I extracted the data from the HTML table using Selenium, structured the data in Python, and then saved it in the CSV format.

### Future Improvements

With more time, or if this were to be turned into a production solution, several additional features and improvements could be considered:

1. Implementing more robust error handling and recovery mechanisms, which could make the scraper more resilient to changes in the website structure or unexpected data formats.
2. Enhancing the data cleaning process by introducing more sophisticated data validation and transformation routines.
3. Adding support for parallel or distributed scraping to speed up the data extraction process.
4. Incorporating an option to store the extracted data in a database, allows for more efficient storage and retrieval of large datasets.
