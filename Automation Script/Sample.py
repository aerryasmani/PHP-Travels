from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# Set up the Chrome webdriver (you can change this to your preferred browser)
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the https://phptravels.net/ website
driver.get("https://phptravels.net/")

# Add a delay for 10 seconds (you can adjust this as needed)
time.sleep(10)

# Find the element using the provided XPath
try:
    element = driver.find_element("xpath", '//*[@id="navbarSupportedContent"]')
    print("Element found using the provided XPath!")
except NoSuchElementException:
    print("Element not found using the provided XPath.")

# Find the button using the defined XPath
button_xpath = '//*[@id="navbarSupportedContent"]'

    
button = driver.find_element("xpath", button_xpath)

# Find the button using the provided XPath
try:
    element = button
    print("Button found using the provided XPath!")
except NoSuchElementException:
    print("Button not found using the provided XPath.")

# Click the button
button.click()

# Add a delay for 10 seconds (you can adjust this as needed)
time.sleep(20)

# Close the browser window
driver.quit()
