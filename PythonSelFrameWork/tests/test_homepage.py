from selenium import webdriver
from selenium.webdriver.support.select import Select
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from testData.HomePageData import HomePageData
import pytest


class TestHomePage(BaseClass):

    def test_formsubmission(self,getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        homepage.getname().clear()
        homepage.getname().send_keys(getData["firstName"])
        homepage.getemail().clear()
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys("password")

        homepage.getcheckbox().click()
        self.selectoption(homepage.getsex(),getData["gender"])

        homepage.getsubmit().click()

        messaage = homepage.getsubmitmsg().text

        assert 'Success!' in messaage

        log.info("profile created for" +getData["firstName"])

    @pytest.fixture(params=HomePageData.gettestData())
    def getData(self,request):
        return request.param

