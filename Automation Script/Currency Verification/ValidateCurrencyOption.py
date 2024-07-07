from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# Open Chrome Browser
options = webdriver.ChromeOptions()
options.add_argument('--log-level=1')
driver = webdriver.Chrome()


# Open Website
driver.get("https://phptravels.net/")


# Maximize Browser
driver.maximize_window()

# Wait for the page to load
WebDriverWait(driver, 30).until(EC.title_contains("PHPTRAVELS"))

time.sleep(5)

# Identify the dropdown element by its XPath
dropdown_xpath = '//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]'

# Click on the dropdown
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
time.sleep(5)
dropdown.click()

# Verify the text presents
element = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]')
language_options = ["USD", "GBP", "SAR","EUR"]
language_results = {}

for language in language_options:
    language_results[language] = language in element.text

for language, result in language_results.items():
    if result:
        print(f"The element contains the language: {language}.")
    else:
        print(f"The element does not contain the language: {language}.")

# Close the WebDriver
driver.quit()