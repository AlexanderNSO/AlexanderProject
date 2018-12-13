from behave import step
from selenium import webdriver


from src.features.pages.login import LoginPage


@step("I open WebPage")
def open_login_page(context):
    context.driver = webdriver.Chrome(executable_path=
                              r"C:\Program Files\JetBrains\PyCharm 2018.1.3 PRO\bin\chromedriver.exe")
    context.driver.implicitly_wait(10)
    context.driver.get("http://lk.qa.cdek.ru/user/login")


@ step("i clicked auth button")
def click_on_auth_button(context):
    authorize = LoginPage(context.driver)
    authorize.click_on_auth_button()