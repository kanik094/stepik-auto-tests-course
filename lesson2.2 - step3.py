from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"


try:

    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text

    func = lambda x, y: str(int(x) + int(y))
    s = func(number1, number2)
    print(type(s))
    print(s)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

    clk = browser.find_element_by_css_selector('[type = "submit"]').click()

finally:
    time.sleep(5)
    browser.quit()
