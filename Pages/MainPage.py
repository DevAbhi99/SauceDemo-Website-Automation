from selenium.webdriver.common.by import By
from Locators.MainLocator import MainLocators


class MainPages:
    def __init__(self, driver):
        self.driver=driver
        self.locator=MainLocators()


    def addToCartElement(self):
        return self.driver.find_element(By.XPATH, self.locator.addToCartXpath)

    def shoppingCartElement(self):
        return self.driver.find_element(By.XPATH, self.locator.shopingCartXpath)

    def checkoutElement(self):
        return self.driver.find_element(By.XPATH, self.locator.checkoutBtnXpath)

    def firstnameElement(self):
        return self.driver.find_element(By.XPATH, self.locator.firstNameXpath)
    
    def lastnameElement(self):
        return self.driver.find_element(By.XPATH, self.locator.lastNameXpath)

    def postalCodeElement(self):
        return self.driver.find_element(By.XPATH, self.locator.postalCodeXpath)

    def continueElement(self):
        return self.driver.find_element(By.XPATH, self.locator.continueBtnXpath)

    def finishElement(self):
        return self.driver.find_element(By.XPATH, self.locator.finishBtnXpath)

    def backhomeElement(self):
        return self.driver.find_element(By.XPATH, self.locator.BackHomeBtnXpath)