from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (make sure you have installed the Selenium package and a compatible WebDriver for your browser)
driver = webdriver.Chrome()

# Open the browser and navigate to the URL
url = "https://www.youtube.com/watch?v=sUcqffQxAeA&ab_channel=TrashTaste"  # Provided YouTube URL
driver.get(url)

# Wait for the span element containing the heading to be present
try:
    heading_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.title"))
    )
    
    # Verify the heading content
    expected_heading = "THINGS WE ACTUALLY LOVE ABOUT JAPAN | Trash Taste 1st Japan Trip"  # Expected heading for the video
    actual_heading = heading_element.get_attribute("innerText")
    
    print("Expected Heading:", expected_heading)
    print("Actual Heading:", actual_heading)
    
    if actual_heading == expected_heading:
        print("Correct Webpage")
    else:
        print("Incorrect Webpage")
        
except Exception as e:
    print("Error occurred:", str(e))

# Close the browser
driver.quit()
