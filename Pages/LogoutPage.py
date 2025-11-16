from selenium.webdriver.common.by import By
from Locators.LogoutLocator import LogoutLocators


class LogoutPages:
    def __init__(self, driver):
        self.driver=driver
        self.locator=LogoutLocators()

    def menuElement(self):
        return self.driver.find_element(By.XPATH, self.locator.menuXpath)

    def logoutElement(self):
        return self.driver.find_element(By.XPATH, self.locator.logoutBtnXpath)

    
