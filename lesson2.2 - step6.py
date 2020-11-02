from selenium import webdriver
import time
import math


link = "http://SunInJuly.github.io/execute_script.html"

def calc(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    value = calc(x)

    button = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element_by_id("answer").send_keys(value)

    click = ("robotCheckbox", "robotsRule",)

    for v in click:
        browser.find_element_by_id(v).click()

    button.click()

finally:
    time.sleep(7)
    browser.quit()

