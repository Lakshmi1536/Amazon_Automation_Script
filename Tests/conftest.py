import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store",default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome()
    elif browser_name=="edge":
        driver= webdriver.Edge()
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    #return driver#it wont work because of yeid keyword
    #so assinging as below
    request.cls.driver = driver
    #action = ActionChains(driver)
    yield
    driver.quit()
