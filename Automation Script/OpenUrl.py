from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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

# Close the browser window
driver.quit()