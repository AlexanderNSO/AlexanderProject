import time

from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(10)

driver.get("https://accounts.google.com")

create_account_button = driver.find_element_by_xpath("//*[text()='Создать аккаунт']")
create_account_button.click()

first_name_field = driver.find_element_by_id("firstName")
first_name_field.send_keys("Alex")

last_name_field = driver.find_element_by_id("lastName")
last_name_field.send_keys("Kardash")

password_field = driver.find_element_by_name("Passwd")
password_field.send_keys("Abc123456!")

confirm_password_field = driver.find_element_by_name("ConfirmPasswd")
confirm_password_field.send_keys("Abc123456!")

username_field = driver.find_element_by_id("username")
username_field.clear()
username_field.send_keys("@a.a")
next_button = driver.find_element_by_id("accountDetailsNext")
next_button.click()
assert "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)." not in driver.page_source
time.sleep(1)

username_field = driver.find_element_by_id("username")
username_field.clear()
username_field.send_keys("a@-a.a")
next_button = driver.find_element_by_id("accountDetailsNext")
next_button.click()
assert "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)." not in driver.page_source
time.sleep(1)

username_field = driver.find_element_by_id("username")
username_field.clear()
username_field.send_keys("a@a@a.a")
next_button = driver.find_element_by_id("accountDetailsNext")
next_button.click()
assert "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)." not in driver.page_source
time.sleep(1)

username_field = driver.find_element_by_id("username")
username_field.clear()
username_field.send_keys("a@a")
next_button = driver.find_element_by_id("accountDetailsNext")
next_button.click()
assert "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)." not in driver.page_source
time.sleep(1)

driver.quit()