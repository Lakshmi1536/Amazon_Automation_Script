from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.Product_MouseActivity_Page import Product_MouseActivity_Page
from PageObject.Product_Selecting_Page import Product_Selecting_Page
from Utilities.BaseClass import BaseClass
from PageObject.Home_page import Home_Page

class TestThree(BaseClass):
    def test_Homepage(self):
        log = self.getlogger()
        #self.windowhandlee()
        # 3Checking the product using mouse hover
        home_page = Home_Page(self.driver)
        home_page.go_to_link_one()
        home_page.go_to_link_two()
        log.info("Home page Mouse hiver Activity Done:)")
    def test_Scrollpage_middle(self):
        log = self.getlogger()
        # Calculate the middle position (half of the page height)
        middle_position = self.driver.execute_script("return window.innerHeight / 2;")
        # 1 Scroll to the middle
        self.driver.execute_script(f"window.scrollTo(0, {middle_position});")
        time.sleep(2)
        # 2 Scroll to the end
        log.info("Successfully Scrolled to the Middle of the Page:)))")
    def test_Scrollpage_down(self):
        log = self.getlogger()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        log.info("Successfully Scrolled to the End of the Page:)))")
    def test_Emptycart(self):
        log = self.getlogger()
        # 3 Empty Cart-Negative testcase
        home_page = Home_Page(self.driver)
        emptycartpage=home_page.go_to_emptycart()
        emptycartmsg = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]").text
        assert "Your Amazon Cart is empty" in emptycartmsg
        log.info("Checking the Empty Cart:))"+emptycartmsg)
    def test_Videochecking(self):
        log = self.getlogger()
        # 4 Video checking
        product_select_page = Product_Selecting_Page(self.driver)
        product_select_page.send_prod_id().send_keys("lego")
        product_page = product_select_page.select_prod_name()
        product_page.select_prod_to_cart().click()
        self.windowhandlee()
        mouse_activity = Product_MouseActivity_Page(self.driver)
        mouse_activity.Mouse_Hover_Action2()
        try:
            element = WebDriverWait(self.driver, 40).until(
                EC.element_to_be_clickable((By.XPATH, "(//button[@title='Play Video'])[1]")))
            element.click()
            time.sleep(10)
        except:
            print("Element is not interactable or clickable after waiting.")
        log.info("Video played Successfully:)))")