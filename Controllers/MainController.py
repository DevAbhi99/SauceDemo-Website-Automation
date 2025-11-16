from Pages.MainPage import MainPages

class MainControllers:

    def __init__(self, driver):
        self.driver=driver
        self.page=MainPages(self.driver)

    def addToCartClick(self):
        return self.page.addToCartElement().click()

    def shoppingCartClick(self):
        return self.page.shoppingCartElement().click()

    def checkoutClick(self):
        return self.page.checkoutElement().click()

    def firstNameFill(self, firstname):
        return self.page.firstnameElement().send_keys(firstname)

    def lastNameFill(self, lastname):
        return self.page.lastnameElement().send_keys(lastname)

    def postalCodeFill(self, postalcode):
        return self.page.postalCodeElement().send_keys(postalcode)

    def continueClick(self):
        return self.page.continueElement().click()

    def finishClick(self):
        return self.page.finishElement().click()

    def backHomeClick(self):
        return self.page.backhomeElement().click()
   