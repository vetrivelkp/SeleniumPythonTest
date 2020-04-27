from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckoutPage


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    password = (By.ID,"exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "input[type=checkbox]")
    sex = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, "[class*=btn-success]")
    submitmsg = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getsex(self):
        return self.driver.find_element(*HomePage.sex)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getsubmitmsg(self):
        return self.driver.find_element(*HomePage.submitmsg)