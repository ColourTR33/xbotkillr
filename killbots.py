
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time


load_dotenv()

# Get the path of the installed ChromeDriver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

username=os.getenv('TWITTER_USERNAME')
password=os.getenv('TWITTER_PASSWORD')

def login_to_x():
    driver.get("https://twitter.com/login")
    time.sleep(5)
    username_field = driver.find_element(By.NAME, "text")
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)
    time.sleep(5)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

    def main():
        login_to_x()
        driver.quit()

        if __name__ == "__name__":
            main()
