from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 15).until(expected_condition, message="Unable to locate element")

    def click_on(self, element):
        self.get_element(element).submit()

    def enter_in(self, element, text):
        self.get_element(element).clear()
        self.get_element(element).send_keys(text)
