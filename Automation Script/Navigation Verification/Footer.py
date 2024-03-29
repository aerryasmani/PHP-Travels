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

# Scroll down to the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(10)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'All Rights Reserved by PHPTRAVELS')]"))
)

# Check if the page is scrolled down
is_scrolled_down = "All Rights Reserved by PHPTRAVELS" in element.text, "Text not found on the page"
time.sleep(3)

if is_scrolled_down:
    print("The page is scrolled down.")
else:
    print("The page is NOT scrolled down.")

#Verify the footer navigations
element = driver.find_element(By.XPATH, '//*[@id="fadein"]/section[2]/div/div[1]/div[1]/div[2]/ul/li/ul')
Navigation_options = ["About Us", "Cookies Policy", "Faq", "Careers And Jobs", "Contact Us","Privacy Policy", "Booking Tips", "How To Book", "Term Of Use", "Become A Supplier","File A Claim"]
Navigation_results = {}

for Navs in Navigation_options:
    Navigation_results[Navs] = Navs in element.text

for Navs, result in Navigation_results.items():
    if result:
        print(f"The element contains the navigation option: {Navs}.")
    else:
        print(f"The element does not contain the navigation option: {Navs}.")
