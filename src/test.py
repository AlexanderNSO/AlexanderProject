from selenium import webdriver

driver = webdriver.Chrome(executable_path=
                          r"C:\Program Files\JetBrains\PyCharm Community Edition 2018.3\bin\chromedriver.exe")
driver.get("https://ru.wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")
search_field.send_keys("Test automation")

search_button = driver.find_element_by_id("searchButton")
search_button.click()

assert "Test automation"in driver.title
assert "tes automation" in driver.page_source

driver.quit()