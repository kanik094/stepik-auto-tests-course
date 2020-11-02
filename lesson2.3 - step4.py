from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[type = 'submit']").click()
    alert = browser.switch_to.alert
    alert.accept()

    value = browser.find_element_by_id("input_value").text

    func = lambda v: str(math.log(abs(12 * math.sin(int(v)))))

    desc = func(value)
    print(desc)

    browser.find_element_by_id("answer").send_keys(desc)

    browser.find_element_by_css_selector("[class = 'btn btn-primary']").click()

finally:

    time.sleep(10)
    browser.quit()