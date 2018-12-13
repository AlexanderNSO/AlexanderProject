from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


from src.features.pages.base_page import BasePage


class LoginPage(BasePage):
    auth_button = (By.XPATH, "//*[@id='login-form']/button")

    def click_on_auth_button(self):
        self.click_on(self.auth_button)
        time.sleep(2)
