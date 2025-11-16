from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from Controllers.LoginController import LoginControllers
from dotenv import load_dotenv
import os

scenarios('Features/Login.feature')


load_dotenv()

base_url=os.getenv('URL')

opts=webdriver.ChromeOptions()
opts.add_argument("--proxy-server='direct://'")
opts.add_argument("--proxy-bypass-list=*")
opts.add_argument("--disable-quic")
# Accept intercepted/self-signed certs if present
opts.set_capability("acceptInsecureCerts", True)
opts.add_argument("--incognito")


service=Service(executable_path='chromedriver.exe')

driver=webdriver.Chrome(service=service, options=opts)


obj1=LoginControllers(driver)

obj2=LoginControllers(driver)


@given('the user is one the login page of the sauce demo website')
def user_is_on_the_login_page():
    
    driver.get(f'{base_url}')

    driver.maximize_window()

    driver.implicitly_wait(10)

    print('User is on the login page')


@when(parsers.parse('the user puts in username "{username}" and password "{password}"'))
def the_user_puts_valid_credentials(username, password):
    time.sleep(1)

    obj1.usernameFill(username)

    time.sleep(1)

    obj1.passwordFill(password)

    time.sleep(1)


@when('the user clicks on the login button')
def the_user_clicks_on_login_btn():
    obj1.loginClick()

    time.sleep(1)


@then('the user gets navigated to the landing page of the website')
def user_navigates_to_landing_page():
    driver.implicitly_wait(10)
    print('logged in with valid credentials')
    time.sleep(1)




