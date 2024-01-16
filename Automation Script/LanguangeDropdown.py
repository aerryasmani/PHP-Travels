from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome Browser
driver = webdriver.Chrome()

# Maximize Browser
driver.maximize_window()

# Open Website
driver.get("https://phptravels.net/")

# Close the browser window
driver.quit()