from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
dropdown.click()

# Wait for the SVG icon to be present for turkish icon
detect_svg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "pk.svg")]')))

if detect_svg:
    detect_svg_src = detect_svg.get_attribute("src")
    print("The SVG is correct and the 'src' attribute value is:", detect_svg_src)
    time.sleep(5)
else:
    print("The SVG is incorrect or not found.")

# Close the WebDriver
driver.quit()
