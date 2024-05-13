from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.Amazon_Page import Amazon_Page
from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_fresh_page(self):
        log=self.getlogger()
        amazon_pages=Amazon_Page(self.driver)
        #self.driver.get_screenshot_as_file("screenFresh.png")
        assert "Fresh" in amazon_pages.getFreshPage(), "You didn't land the page correctly!!! "
        log.info("Fresh Page is Executed Successfully:)")
        self.driver.refresh()

    def test_minitv_page(self):
        log=self.getlogger()
        amazon_pages=Amazon_Page(self.driver)
        log.info("Getting MiniTv Page Title Assertion")
        assert "Amazon miniTV" in amazon_pages.getMinitvPage(), "You didn't land the page correctly!!! "
        log.info("Minitv Page is Executed Successfully:)")
        self.driver.get_screenshot_as_file("screenFresh.png")
        amazon_pages.getGoToShop()

    def test_sell_page(self):
        log=self.getlogger()
        amazon_pages=Amazon_Page(self.driver)
        assert "Start Selling" in amazon_pages.getSellPage(), "You didn't land the page correctly!!! "
        log.info("Sell Page is Executed Successfully:)")

    def test_best_seller_page(self):
        log=self.getlogger()
        amazon_pages=Amazon_Page(self.driver)
        assert "Bestseller" in amazon_pages.getBestsellerPage(), "You didn't land the page correctly!!! "
        log.info("Best Seller Page is Executed Successfully:)")

    def test_todays_deal_page(self):
        log=self.getlogger()
        amazon_pages=Amazon_Page(self.driver)
        assert "Deals" in amazon_pages.getTodaysDealPage(), "You didn't land the page correctly!!! "
        log.info("Today's Deal Page is Executed Successfully:)")

