from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# Open Chrome Browser with ignore certificate errors option
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

#Maximize Browser
driver.maximize_window()

#Open Website
driver.get("https://phptravels.net/")

# Add a delay for 10 seconds (you can adjust this as needed)
time.sleep(10)

#Print Title
print(driver.title)

# Close the browser window
driver.quit()