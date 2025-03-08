from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Open Instagram URL
driver.get("https://www.instagram.com/guviofficial/")

# Wait for the followers and following elements to be loaded
time.sleep(5)

# Extract the number of followers and following using XPATH
followers = driver.find_element(By.XPATH, "//a[contains(@href,'/followers')]/span")
following = driver.find_element(By.XPATH, "//a[contains(@href,'/following')]/span")

# Print the results
print(f"Followers: {followers.text}")
print(f"Following: {following.text}")

# Close the browser
driver.quit()
