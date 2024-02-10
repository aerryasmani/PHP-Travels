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

# Wait for the SVG icon to be present for turkish icon
detect_svg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[contains(@src, "tr.svg")]')))

if detect_svg:
    detect_svg_src = detect_svg.get_attribute("src")
    print("The SVG is correct and the 'src' attribute value is:", detect_svg_src)
    time.sleep(5)
else:
    print("The SVG is incorrect or not found.")

# Close the WebDriver
driver.quit()
