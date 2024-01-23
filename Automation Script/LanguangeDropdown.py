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

time.sleep(5)

# Identify the dropdown element by its XPath
dropdown_xpath = '//*[@id="navbarSupportedContent"]/div[2]/ul/li[1]/a'

# Click on the dropdown
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
time.sleep(5)
dropdown.click()

# Verify the text presents
element = driver.find_element(By.XPATH, "//body/header/div/div[2]/div[2]/ul/li[1]/ul/li[1]/a")
search_text = "English"
if search_text in element.text:
    print(f"The element contains the {search_text}.")
else:
    print(f"The element does not contain the search text: {search_text}.")

# Click on the dropdown
#Verify the choosen option
#Click the option
#Other operations
#Close dropdown
#Delay to make sure everything is close
time.sleep(5)

# Close the browser window
driver.quit()
