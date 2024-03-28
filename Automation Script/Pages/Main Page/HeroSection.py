from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Import TimeoutException
import time

# Open Chrome Browser
driver = webdriver.Chrome()
driver.delete_all_cookies()
time.sleep(5)

# Open Website
driver.get("https://phptravels.net/")

# Maximize Browser
driver.maximize_window()

# Wait for the page to load
try:
    WebDriverWait(driver, 30).until(EC.title_contains("Your Trip Starts Here!"))
except TimeoutException:
    print("Timeout: Page title did not contain expected text.")

# Wait for the element to be visible
element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h4[@class='text-white']")))

# Extract the text of the element
text = element.text

if "Your Trip Starts Here!" in text:
    print("Text is present on the page.")
    print(text)  # Print the text of the element
else:
    print("Text is not present on the page.")
