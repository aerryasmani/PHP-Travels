from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.support.ui import Select

# Open Chrome Browser
driver = webdriver.Chrome()

# Open Website
driver.get("https://phptravels.net/")

# Maximize Browser
driver.maximize_window()

# Wait for the page to load
WebDriverWait(driver, 30).until(
    EC.title_contains("PHPTRAVELS")
)

# Identify the dropdown element by its XPath
dropdown_xpath = '//*[@id="navbarSupportedContent"]/div[2]/ul/li[1]/a'

# Increase the timeout for the WebDriverWait
wait = WebDriverWait(driver, 30)

# Click on the dropdown
#Verify the choosen option
#Click the option
#Close dropdown

# Delay to make sure everything is close
time.sleep(5)

# Close the browser window
driver.quit()
