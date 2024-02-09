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
dropdown_xpath = '//*[@id="navbarSupportedContent"]/div[2]/ul/li[1]/a'

# Click on the dropdown
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
time.sleep(5)
dropdown.click()

# Verify the text presents
element = driver.find_element(By.XPATH, "//header/div/div[2]/div[2]/ul/li[1]/ul")
language_options = ["English", "Arabic", "Turkish", "Russian", "French", "Chinese", "Germany"]
language_results = {}

for language in language_options:
    language_results[language] = language in element.text

for language, result in language_results.items():
    if result:
        print(f"The element contains the language: {language}.")
    else:
        print(f"The element does not contain the language: {language}.")

# Click on the language option
language_options = driver.find_elements(By.XPATH, '//ul[@class="dropdown-menu rounded-1 show"]//a')
time.sleep(5)

if len(language_options) >= 4:  # Check if the desired index is within range
    desired_option = language_options[2]  # Change the index to select a different option
    desired_option.click()
    print("This is the correct option")
    time.sleep(5)
else:
    print("Desired option not available. Please choose an index within range.")
    time.sleep(5)

#Text Present or not

# Close the browser window
driver.quit()
