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

# Verify the navigation text presents
element = driver.find_element(By.XPATH, "//ul[@class='header_menu navbar-nav']/li[position() >= 1 and position() <= 5]/a")
Navigation_options = ["Flights", "Hotels", "Tours", "Cars", "Blogs"]
Navigation_results = {}

for Navs in Navigation_options:
    Navigation_results[Navs] = Navs in element.text

for Navs, result in Navigation_results.items():
    if result:
        print(f"The element contains the navigation option: {Navs}.")
    else:
        print(f"The element does not contain the navigation option: {Navs}.")

#Click on The Navigation And Redirection
for Navs in Navigation_options:
    Navigation_element = driver.find_element(By.XPATH, "//ul[@class='header_menu navbar-nav']/li[position() >= 1 and position() <= 5]/a")
    Navigation_element.click()

#Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

try:
    WebDriverWait(driver, 10).until(EC.url_contains(Navs.lower()))
    Navigation_results[Navs] = True
    print(f"The navigation option '{Navs}' is present.")
except:
    Navigation_results[Navs] = False
    print(f"The navigation option '{Navs}' is not present.")

#Delay Time
time.sleep(10)    

# Go back to the previous page
driver.back()