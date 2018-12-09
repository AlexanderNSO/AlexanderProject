import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=
                          r"C:\Program Files\JetBrains\PyCharm Community Edition 2018.3\bin\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://accounts.google.com")

create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()

email_set = ["ddswwww@a.agfd", "aewqew@-a.a", "eqwea@a@a.a" "dasdfha@a"]
user_dictionary = {"firstName": "Alex", "lastName": "Khudyaev", "Passwd": "QWErty123456"}

first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
confirm_password_field = driver.find_element_by_name("ConfirmPasswd")
username_field = driver.find_element_by_id("username")
next_button = driver.find_element_by_id("accountDetailsNext")
validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."

def validate_username_field(email):
    username_field.clear()
    username_field.send_keys(email)
    next_button.click()
    assert validation_error not in driver.page_source
    time.sleep(1)

first_name_field.send_keys(user_dictionary["firstName"])
last_name_field.send_keys(user_dictionary["lastName"])
password_field.send_keys(user_dictionary["Passwd"])
confirm_password_field.send_keys(user_dictionary["Passwd"])

for i in email_set:
    validate_username_field(i)


driver.quit()