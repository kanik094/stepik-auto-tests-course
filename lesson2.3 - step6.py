from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("button").click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text

    func = lambda v: str(math.log(abs(12 * math.sin(int(v)))))

    browser.find_element_by_id("answer").send_keys(func(x))

    browser.find_element_by_css_selector("[type = 'submit']").click()

finally:
    time.sleep(10)
    browser.quit()



