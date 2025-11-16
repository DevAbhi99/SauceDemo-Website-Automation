from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from dotenv import load_dotenv
import os
from Controllers.LoginController import LoginControllers
from Controllers.MainController import MainControllers
from Controllers.LogoutController import LogoutControllers
from pytest_bdd import scenarios, given, when, then


scenarios('Features/Main.feature')

load_dotenv()

url=os.getenv('URL')

username=os.getenv('USER')

password=os.getenv('PASSWORD')

firstname=os.getenv('FIRST_NAME')

lastname=os.getenv('LAST_NAME')

postalcode=os.getenv('POSTAL_CODE')

base_url=f"{url}"

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

obj2=MainControllers(driver)

obj3=LogoutControllers(driver)

@given('the user is on the landing page of the website')
def user_is_on_the_landing_page_of_the_website():
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

    print('The user is on the landing page of the website!')


@when('the user is on the landing page then the user clicks on add to cart of a button and proceed to click on the shopping cart button')
def user_clicks_on_addtocart_and_shoppingcart_button():
    obj2.addToCartClick()

    time.sleep(1)

    obj2.shoppingCartClick()

    time.sleep(1)




@when('the user is navigated to the checkout page where the user clicks on the checkout button')
def user_navigates_to_checkout():
      obj2.checkoutClick()

      time.sleep(1)


@when('the user is navigated to the information page then the user is provides valid information and clicks on continue button')
def user_navigates_to_information_page():
    obj2.firstNameFill(f'{firstname}')

    time.sleep(1)

    obj2.lastNameFill(f'{lastname}')

    time.sleep(1)

    obj2.postalCodeFill(f'{postalcode}')

    time.sleep(1)

    obj2.continueClick()

    time.sleep(1)


@when('the the user is navigated to the description page where the user has to click on the Finish button')
def user_navigates_to_description_page():
    obj2.finishClick()

    time.sleep(2)

    driver.save_screenshot('scnreeshots/checkout.png')


@when('the user is navigated to final checkout page and the user clicks on the Back home button')
def user_navigates_to_final_chekoutpage():
    obj2.backHomeClick()

    time.sleep(2)


@then('the user is navigated back to landing page of the website')
def user_navigates_back_to_landingpage():
    driver.implicitly_wait(10)

    print('User is on the landing page')

    obj3.menuClick()

    time.sleep(1)

    obj3.logoutClick()

    time.sleep(1)

    driver.quit()
