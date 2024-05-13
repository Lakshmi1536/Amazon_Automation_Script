from selenium.webdriver.common.by import By
class Amazon_Page:
    def __init__(self,driver):
        self.driver=driver

    FreshPage=(By.LINK_TEXT,"Fresh")
    MiniTvPage = (By.LINK_TEXT,"Amazon miniTV")
    Gotoshop= (By.XPATH, "//*[text()='Go to Amazon Shopping']")
    SellPage = (By.LINK_TEXT, "Sell")
    BestSellerPage = (By.LINK_TEXT, "Best Sellers")
    TodayDealPage = (By.LINK_TEXT, "Today's Deals")

    def getFreshPage(self):
        self.driver.find_element(*Amazon_Page.FreshPage).click()
        return self.driver.title
    def getMinitvPage(self):
        self.driver.find_element(*Amazon_Page.MiniTvPage).click()
        return self.driver.title
    def getGoToShop(self):
        return self.driver.find_element(*Amazon_Page.Gotoshop).click()
    def getSellPage(self):
        self.driver.find_element(*Amazon_Page.SellPage).click()
        return self.driver.title
    def getBestsellerPage(self):
        self.driver.find_element(*Amazon_Page.BestSellerPage).click()
        return self.driver.title
    def getTodaysDealPage(self):
        self.driver.find_element(*Amazon_Page.TodayDealPage).click()
        return self.driver.title




