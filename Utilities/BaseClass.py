import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID,"nav-cart-text-container")))

    def windowhandlee(self):
        windowsopened = self.driver.window_handles
        self.driver.switch_to.window(windowsopened[1])

    #     dropdown = Select(locator)
    #     dropdown.select_by_visible_text(text)
