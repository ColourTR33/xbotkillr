
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
default_sleep=os.getenv('DEFAULT_SLEEP')

def login_to_x():
    driver.get("https://twitter.com/login")
    time.sleep(default_sleep)
    print("Please enter login credentials")
    input("Press enter here when you have sucessfully logged in")
    
    def main():
        login_to_x()
        driver.quit()

        if __name__ == "__name__":
            main()
