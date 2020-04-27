import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def objectpresence(self,locatorobj):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, locatorobj)))

    def selectoption(self,element, option):
        select = Select(element)
        select.select_by_visible_text(option)

    def getlogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        #Provide file location
        file = logging.FileHandler("logfile.log")
        logger.addHandler(file) #filehandler object

        #File Format
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file.setFormatter(formatter)

        #LoggingLevel
        logger.setLevel(logging.INFO)
        return logger
