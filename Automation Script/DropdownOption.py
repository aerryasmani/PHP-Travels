from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Open Chrome Browser with ignore certificate errors option
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)


# Maximize Browser
driver.maximize_window()

# Open Website\
driver.get("https://phptravels.net/")

# Wait for the page to load
WebDriverWait(driver, 20).until(
    EC.title_contains("PHPTRAVELS")
)

# Identify the dropdown element by its XPath
dropdown_xpath = '//*[@id="navbarSupportedContent"]/div[2]/ul/li[1]/a'

# Click on the dropdown
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
dropdown.click()

# Define the option XPath after clicking on the dropdown
option_text_to_select = "Option to Select"
option_xpath = f'//a[contains(text(), "{option_text_to_select}")]'

# Wait for the option to be visible after clicking on the dropdown
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# Select an option from the dropdown
try:
    option = driver.find_element(By.XPATH, option_xpath)
    option.click()
    print(f"Option '{option_text_to_select}' found and clicked.")
except Exception as e:
    print(f"Error: {e}")

# Verify that the selected option is correct
selected_option = option.text if option else None
expected_option = "Option to Select"

if selected_option == expected_option:
    print(f"Test Passed: Dropdown option '{expected_option}' is selected.")
else:
    print(f"Test Failed: Expected '{expected_option}' but got '{selected_option}'.")

# Verify Header Of the Page
header_element = driver.find_element(By.CLASS_NAME, "text-white")
header_text = header_element.text
expected_header_text = "Your Trip Starts Here!"
assert header_text == expected_header_text, f"Header text is not as expected. Found: {header_text}, Expected: {expected_header_text}"

# Close the browser window
driver.quit()