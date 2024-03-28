from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# Open Chrome Browser
driver = webdriver.Chrome()

# Open Website
driver.get("https://phptravels.net/")

# Maximize Browser
driver.maximize_window()

# Wait for the page to load
WebDriverWait(driver, 30).until(EC.title_contains("PHPTRAVELS"))

time.sleep(5)

# Identify the dropdown element by its XPath
dropdown_xpath = '//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a'

# Click on the dropdown
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
time.sleep(5)
dropdown.click()

# Verify the text presents
element = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/ul')
language_options = ["IND", "PAK", "BAN"]
language_results = {}

for language in language_options:
    language_results[language] = language in element.text

for language, result in language_results.items():
    if result:
        print(f"The element contains the language: {language}.")
    else:
        print(f"The element does not contain the language: {language}.")

# Click on the language option
language_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/currency/PAK')]")))
if language_option:
    language_option.click()
    time.sleep(10)
    print("This is the correct currency")
else:
    print("This is the incorrect")

# Close the WebDriver
driver.quit()