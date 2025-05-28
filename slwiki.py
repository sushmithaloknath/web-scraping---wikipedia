from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start the browser
driver = webdriver.Chrome()

# Open Wikipedia
driver.get("https://www.wikipedia.org/")

# Locate search box and enter a query
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Artificial Intelligence")
search_box.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(2)

# Extract all paragraphs and find the first non-empty one
paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
for para in paragraphs:
    if para.text.strip():  # Ignore empty paragraphs
        print("Wikipedia Summary:", para.text)
        break  # Print only the first meaningful paragraph

# Close the browser
driver.quit()
