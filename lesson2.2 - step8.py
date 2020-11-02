from selenium import webdriver
import time
import os.path

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[name = 'firstname']").send_keys("Ivan")
    browser.find_element_by_css_selector("[name = 'lastname']").send_keys("Davidoff")
    browser.find_element_by_css_selector("[name = 'email']").send_keys("kantik007@bk.ru")

    path = r"D:\1.txt"

    browser.find_element_by_id("file").send_keys(path)

    browser.find_element_by_css_selector("[class = 'btn btn-primary']").click()

finally:
    time.sleep(10)
    browser.quit()


