from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#Open Chrome Browser
driver = webdriver.Chrome()

#Maximize Browser
driver.maximize_window()

#Open Website
driver.get("https://phptravels.net/")

# Add a delay for 10 seconds (you can adjust this as needed)
time.sleep(10)

#Print Title
print(driver.title)

#Verify Dropdown Option
# Locate the dropdown element
dropdown = Select(driver.find_element(By.XPATH, "//*[@id='navbarSupportedContent']/div[2]/ul/li[1]/ul"))

# Select an option by value
dropdown.select_by_value("English")

#Verify Header Of the Page
header_element = driver.find_element_by_class_name ("text-white")
header_text = header_element.text
expected_header_text = "Your Trip Starts Here!"
assert header_text == expected_header_text, f"Header text is not as expected. Found: {header_text}, Expected: {expected_header_text}"

# Close the browser window
driver.quit()