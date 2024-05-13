from selenium.webdriver.common.by import By
class Product_Page:
    def __init__(self,driver):
        self.driver=driver

    Prod_To_Cart=(By.XPATH,"//*[text()='LEGO Medium Creative Brick Box,Creative Thinking,Multicolor, 484 Pcs']")
    def select_prod_to_cart(self):
        return self.driver.find_element(*Product_Page.Prod_To_Cart)