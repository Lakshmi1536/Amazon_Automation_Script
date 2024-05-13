from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class Empty_Cart_Page:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    textmsg = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty'")

    def emptymsg(self):
        return self.driver.find_element(*Empty_Cart_Page.textmsg).text
