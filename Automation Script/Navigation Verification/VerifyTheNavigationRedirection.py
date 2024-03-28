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
element = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul')
Navigation_options = ["Flights", "Hotels", "Tours", "Cars", "Blogs"]
Navigation_results = {}

#Click on The Navigation And Redirection
for option_text in Navigation_options:
    try:
        Navigation_element = driver.find_element(By.XPATH, f'//ul[@class="header_menu navbar-nav"]/li/a[contains(@class, "nav-link") and text()="{option_text}"]')
        Navigation_element.click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul')))
        
        WebDriverWait(driver, 10).until(EC.url_contains(option_text.lower()))
        
        Navigation_results[option_text] = True
        print(f"Navigate to '{option_text}' page.")
        time.sleep(10)  # Optional: Add a delay for demonstration purposes
        
        driver.back()
    except Exception as e:
        Navigation_results[option_text] = False
        print(f"Fail to navigate '{option_text}' page:", e)

 

