from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageObject.Empty_Cart_Page import Empty_Cart_Page


class Home_Page:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    link1=(By.CLASS_NAME, "icp-nav-link-inner")
    link2=(By.ID, "nav-link-accountList-nav-line-1")
    emptycart=(By.ID, "nav-cart-count")
    emptycartpage = (By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty'")


    def go_to_link_one(self):
        return self.action.move_to_element(self.driver.find_element(*Home_Page.link1)).perform()
    def go_to_link_two(self):
        return self.action.move_to_element(self.driver.find_element(*Home_Page.link2)).perform()
    def go_to_emptycart(self):
        self.driver.find_element(*Home_Page.emptycart).click()
        emptycartpage=Empty_Cart_Page(self.driver)
        return emptycartpage

