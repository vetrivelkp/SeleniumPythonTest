from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass

class ConfirmPage:

    location = (By.ID, "country")
    selectloc = (By.LINK_TEXT, "India")
    termsandcond = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    submitmessage = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver


    def getlocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    def getselectloc(self):
        return self.driver.find_element(*ConfirmPage.selectloc)

    def gettermsandcond(self):
        return self.driver.find_element(*ConfirmPage.termsandcond)

    def getsubmit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def getsubmitmessage(self):
        return self.driver.find_element(*ConfirmPage.submitmessage)

