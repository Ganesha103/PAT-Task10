from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class InstagramProfile:
    """Instagram Profile Automation using Selenium"""
    def __init__(self, profile_url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(profile_url)
        self.driver.implicitly_wait(10)  # Wait for elements to load

    def get_followers_following(self):
        """Extract Followers & Following Count"""
        followers_xpath = "//a[contains(@href,'/followers')]/span"  # Relative XPath
        following_xpath = "//a[contains(@href,'/following')]/span"  # Relative XPath

        followers = self.driver.find_element(By.XPATH, followers_xpath).text
        following = self.driver.find_element(By.XPATH, following_xpath).text

        return {"followers": followers, "following": following}

    def close_browser(self):
        """Close the browser session"""
        self.driver.quit()

# Usage Example
profile = InstagramProfile("https://www.instagram.com/guviofficial/")
data = profile.get_followers_following()
print(f"Followers: {data['followers']}, Following: {data['following']}")
profile.close_browser()
