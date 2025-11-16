from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from Controllers.LoginController import LoginControllers
from Controllers.LogoutController import LogoutControllers
from Data.ItemsData import ItemData
from pytest_bdd import scenarios, given, when, then
from dotenv import load_dotenv
import os

scenarios('Features/verifyItems.feature')


load_dotenv()

url=os.getenv('URL')

base_url=f'{url}'

username=os.getenv('USER')

password=os.getenv('PASSWORD')


opts=webdriver.ChromeOptions()
opts.add_argument("--proxy-server='direct://'")
opts.add_argument("--proxy-bypass-list=*")
opts.add_argument("--disable-quic")
# Accept intercepted/self-signed certs if present
opts.set_capability("acceptInsecureCerts", True)
opts.add_argument("--incognito")
# Docker/Jenkins compatibility options
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1920,1080")

# Use system chromedriver (no hardcoded path needed)
driver=webdriver.Chrome(options=opts)

obj1=LoginControllers(driver)

obj2=ItemData()

obj3=LogoutControllers(driver)





@given('the user is on the landing page of the website')
def user_is_on_the_landingpage():
    driver.get(base_url)

    driver.maximize_window()

    driver.implicitly_wait(10)

    time.sleep(1)

    obj1.usernameFill(f'{username}')

    time.sleep(1)

    obj1.passwordFill(f'{password}')

    time.sleep(1)

    obj1.loginClick()

    time.sleep(1)

    driver.implicitly_wait(10)

    print('The user is on the landing page')


@then('the user clicks on the title of each item and automated verification is done')
def user_verifies_titles():
    driver.execute_script('window.scrollBy(0,100);')

    arr=obj2.data

    for i in range(0, len(arr)):
        title=driver.find_element(By.XPATH, f"//div[@class='inventory_container']/div[1]/div[{i+1}]/div[2]/div[1]/a[1]/div[1]").text
        price=driver.find_element(By.XPATH, f"//div[@class='inventory_container']/div[1]/div[{i+1}]/div[2]/div[2]/div[1]").text
        
        assert title==arr[i]['name']
        assert price==arr[i]['price']
        print(title)
        print(price)
        time.sleep(1)
        
    driver.quit()


