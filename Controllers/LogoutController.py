from Pages.LogoutPage import LogoutPages

class LogoutControllers:

    def __init__(self, driver):
        self.driver=driver
        self.page=LogoutPages(self.driver)

    
    def menuClick(self):
        return self.page.menuElement().click()

    def logoutClick(self):
        return self.page.logoutElement().click() 
