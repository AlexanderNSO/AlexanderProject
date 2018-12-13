from selenium.webdriver.common.by import By
from src.features.pages.base_page import BasePage


class AuthorizeStep(BasePage):
    user_field = (By.ID, "loginform-login")
    password = (By.ID, "loginform-password")

    def enter_text_in_form_login(self, text):
        self.get_element(self.user_field).send_keys(text)

    def enter_text_in_form_password(self, text):
        self.get_element(self.password).send_keys(text)