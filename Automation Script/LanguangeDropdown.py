from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Set up the Chrome webdriver (you can change this to your preferred browser)
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the https://phptravels.net website
driver.get("https://phptravels.net")

# Find the element using the provided XPath
try:
    element = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[1]/ul')
    print("Element found using the provided XPath!")

    # Add a delay for 10 seconds (you can adjust this as needed)
    time.sleep(10)

    # Find the button using the defined XPath
    button_xpath = '//*[@id="navbarSupportedContent"]/div[2]/ul/li[1]/ul'
    button = driver.find_element(By.XPATH, button_xpath)

    # Find the button using the provided XPath
    try:
        element = button
        print("Button found using the provided XPath!")
        
        # Wait for the element with the specified class to be present
        element_class = "nav-item dropdown"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, element_class))
        )

        # Perform actions with the located element
        # For example, clicking on the element
        element.click()

    except NoSuchElementException:
        print("Button not found using the provided XPath.")

except NoSuchElementException:
    print("Element not found using the provided XPath.")

except TimeoutException:
    print(f"Timeout waiting for element with class '{element_class}' to be present.")

# Close the browser
driver.quit()
