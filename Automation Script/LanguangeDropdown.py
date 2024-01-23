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
try:
    dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown.click()
except TimeoutException as e:
    print(f"TimeoutException: {e}")

#Verify dropdown options
def verifyTextPresent(text_to_verify, dropdown_options):
    return text_to_verify in dropdown_options

def verify_dropdown(text_list, dropdown_options):
    for text_to_verify in text_list:
        while not verifyTextPresent(text_to_verify, dropdown_options):
            print(f"Text '{text_to_verify}' not found in the dropdown. Retrying...")
    print("Verification complete for all texts.")

# Example usage:
dropdown_options = ["English", "Arabic", "Turkish"]

text_list_to_verify = ["English", "Arabic", "Turkish"]

verify_dropdown(text_list_to_verify, dropdown_options)

#Verify the choosen option
#Click the option
#Close dropdown

# Delay to make sure everything is close
time.sleep(5)

# Close the browser window
driver.quit()
