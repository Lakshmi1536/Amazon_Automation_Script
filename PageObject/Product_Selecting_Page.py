from selenium.webdriver.common.by import By

from PageObject.Product_Page import Product_Page


class Product_Selecting_Page:
    def __init__(self,driver):
        self.driver=driver

    Prod_ID=(By.ID,"twotabsearchtextbox")
    Prod_Name=(By.XPATH,"//*[text()=' blocks for boys 7-14 years']")

    def send_prod_id(self):
        return self.driver.find_element(*Product_Selecting_Page.Prod_ID)
    def select_prod_name(self):
        self.driver.find_element(*Product_Selecting_Page.Prod_Name).click()
        product_page=Product_Page(self.driver)
        return product_page