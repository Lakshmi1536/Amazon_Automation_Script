from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from PageObject.Product_Selecting_Page import Product_Selecting_Page
from PageObject.Product_MouseActivity_Page import Product_MouseActivity_Page
from PageObject.Checkout_Page import Checkout_Page

class Test_two(BaseClass):
    def test_ProductSelecting(self):
        #1 selecting the product
        log = self.getlogger()
        product_select_page = Product_Selecting_Page(self.driver)
        product_select_page.send_prod_id().send_keys("lego")
        log.info("Sending The Product key!!!")
        product_page=product_select_page.select_prod_name()
        log.info("Selecting The Product!!!")
        # 2 Adding the product to the cart
        product_page.select_prod_to_cart().click()
        log.info("Adding The Product to the Cart!!!")
        self.windowhandlee()
        # 3Checking the product using mouse hover
        mouse_activity=Product_MouseActivity_Page(self.driver)
        mouse_activity.Mouse_Hover_Action1()
        mouse_activity.Mouse_Hover_Action2()
        mouse_activity.Mouse_Hover_Action3()
        mouse_activity.Mouse_Hover_Action4()
        mouse_activity.Mouse_Hover_Action5()
        mouse_activity.Mouse_Hover_Action6()
        mouse_activity.Mouse_Hover_Action7()
        # 4 Increasing the quantity to 2
        mouse_activity.Product_count_Increase()
        log.info("Successfully Mouse Hover Activity done:)")
        #5Evaluating cart to proceed to checkout page
        mouse_activity.Product_Checkout()
        self.verifyLinkPresence()
        proceed_to_checkout = self.driver.title
        assert "Shopping Cart" in proceed_to_checkout, "You didn't land the page correctly!!! "
        log.info("Landed on Checkout page:))")
        checkout=Checkout_Page(self.driver)
        checkout.Proceed_To_Checkout()

