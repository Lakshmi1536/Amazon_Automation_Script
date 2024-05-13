from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Product_MouseActivity_Page:
    def __init__(self,driver):
        self.driver=driver
        self.action= ActionChains(driver)
    act1=(By.ID,"a-autoid-3")
    act2=(By.ID,"a-autoid-4")
    act3=(By.ID,"a-autoid-5")
    act4=(By.ID,"a-autoid-6")
    act5=(By.ID,"a-autoid-7")
    act6=(By.ID,"a-autoid-8")
    act7=(By.ID,"a-autoid-9")
    prodcount=(By.ID, "quantity")
    productincrease=(By.XPATH, "//option[@value='2']")
    producttocart=(By.ID,"add-to-cart-button")
    def Mouse_Hover_Action1(self):
        #return self.driver.find_element(*Product_MouseHover_Page.act1)
        return self.action.move_to_element(self.driver.find_element(*Product_MouseActivity_Page.act1)).perform()
    def Mouse_Hover_Action2(self):
        return self.action.move_to_element(self.driver.find_element(*Product_MouseActivity_Page.act2)).perform()
    def Mouse_Hover_Action3(self):
        return self.action.move_to_element(self.driver.find_element(*Product_MouseActivity_Page.act3)).perform()
    def Mouse_Hover_Action4(self):
        return self.action.move_to_element(self.driver.find_element(*Product_MouseActivity_Page.act4)).perform()
    def Mouse_Hover_Action5(self):
        return self.action.move_to_element(self.driver.find_element(*Product_MouseActivity_Page.act5)).perform()
    def Mouse_Hover_Action6(self):
        return self.action.move_to_element(self.driver.find_element(*Product_MouseActivity_Page.act6)).perform()
    def Mouse_Hover_Action7(self):
        return self.action.move_to_element(self.driver.find_element(*Product_MouseActivity_Page.act7)).perform()

    def Product_count_Increase(self):
        self.driver.find_element(*Product_MouseActivity_Page.prodcount).click()
        return self.driver.find_element(*Product_MouseActivity_Page.productincrease).click()
    def Product_Checkout(self):
        return self.driver.find_element(*Product_MouseActivity_Page.producttocart).click()