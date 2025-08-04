import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

@pytest.fixture()
#def driver():
#    driver = webdriver.Chrome()
#    yield driver
#    driver.quit()
def driver():
#    options = ChromeOptions()
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options)
    yield driver
    driver.quit()