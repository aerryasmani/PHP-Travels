import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO
logger = logging.getLogger(__name__)  # Create a logger for the script

try:
    # Initialize the WebDriver
    logger.info("Initializing WebDriver...")
    driver = webdriver.Chrome()
    logger.info("WebDriver initialized.")

    # Open the browser and navigate to the URL
    url = "https://www.youtube.com/watch?v=I8BobmZglOk&ab_channel=ScreenJunkies"
    logger.info(f"Opening URL: {url}")
    driver.get(url)
    logger.info("URL opened.")

    # Wait for the span element containing the heading to be present
    logger.info("Waiting for heading element...")
    heading_element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.title"))
    )
    logger.info("Heading element found.")

    # Verify the heading content
    expected_heading = "Honest Trailers - X-Men: The Animated Series"
    actual_heading = heading_element.get_attribute("innerText")
    logger.info(f"Expected Heading: {expected_heading}")
    logger.info(f"Actual Heading: {actual_heading}")

    if actual_heading == expected_heading:
        logger.info("Correct Webpage")
    else:
        logger.info("Incorrect Webpage")

except Exception as e:
    logger.error(f"Error occurred: {str(e)}")

finally:
    # Close the browser
    logger.info("Closing the browser.")
    driver.quit()
    logger.info("Browser closed.")
