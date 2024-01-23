from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

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
try:
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown.click()
except TimeoutException as e:
    print(f"TimeoutException: {e}")

# Adding a small delay for demonstration purposes (you can remove this in your actual script)
time.sleep(5)

# Close the browser window
driver.quit()
