from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
WebDriverWait(driver, 30).until(EC.title_contains("PHPTRAVELS"))

time.sleep(5)

#Verify the text of the search bar is present
WebDriverWait(driver, 30).until(EC.title_contains("Your Trip Starts Here!"))
time.sleep(5)
Text = driver.find_element(By.XPATH, "//h4[@class='text-white']")

if "Your Trip Starts Here!" in Text:
    print("Text is present on the page.")
    print(Text)  # Print the text of the element
else:
    print("Text is not present on the page.")