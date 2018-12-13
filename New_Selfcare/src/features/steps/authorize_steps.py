from behave import  step

from src.features.pages.auth_pages import AuthorizeStep

@step ("i Filled in the authorization form")
def fill_authorize(context):
    authorize_step = AuthorizeStep(context.driver)
    authorize_step.enter_text_in_form_login("П_ТЕСТ")
    authorize_step.enter_text_in_form_password("654321")

