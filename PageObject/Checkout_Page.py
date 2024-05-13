from selenium.webdriver.common.by import By

class Checkout_Page:
    def __init__(self,driver):
        self.driver=driver

    proceed_button=(By.XPATH, "//input[@name='proceedToRetailCheckout']")

    def Proceed_To_Checkout(self):
        self.driver.find_element(*Checkout_Page.proceed_button).click()
