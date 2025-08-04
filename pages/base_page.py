from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self,locator):
        self.driver.find_element(*locator).click()

    def enter_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_invis_element(self, locator):
        return self.driver.find_element(*locator)

    def go_to_url(self, url):
        self.driver.get(url)