from selenium.webdriver.common.by import By

from pageObject.Confirm import ConfirmPage


class CheckoutPage:

    ProductsTitle = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    AddtoCart = (By.XPATH, "//div/div/button")
    checkoutinshop = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutincart = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getproductstitle(self):
        return self.driver.find_elements(*CheckoutPage.ProductsTitle)

    def getaddtocart(self):
        return self.driver.find_elements(*CheckoutPage.AddtoCart)

    def getcheckoutinshop(self):
        return self.driver.find_element(*CheckoutPage.checkoutinshop)

    def getcheckoutincart(self):
        self.driver.find_element(*CheckoutPage.checkoutincart).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage