from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# URL of the web page with the download button
url = 'https://www.whoisds.com/newly-registered-domains'
driver.get(url)
time.sleep(3)
# Locate the download button element (replace with appropriate locator)
download_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[1]/div[2]/div/table/tbody/tr[2]/td[4]/a/button')

# Perform a click action to initiate the download
download_button.click()
time.sleep(3)
driver.quit()

# Optionally, you can wait for the download to complete using WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the source and destination paths
downloaded_file_source = r'C:/Users/Yash Thakar/Downloads/newly-registered-domains-2023-10-03.zip'  # Update with the actual download path
custom_destination_folder = r'C:/Users/Yash Thakar/PROGRAMMING/storm_technocrats/Backend/cdv'  # Replace with your custom folder path

import shutil

# Move the downloaded file to the custom folder
shutil.copyfile(downloaded_file_source, custom_destination_folder)


# Wait until the file is downloaded
# wait = WebDriverWait(driver, 100)
