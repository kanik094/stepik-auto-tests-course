from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/math.html"


try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    find_text_element = browser.find_element_by_id("input_value")
    x = find_text_element.text
    y = calc(x)

    input_text = browser.find_element_by_id("answer")
    input_text.send_keys(y)

    click_checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    click_checkbox.click()

    click_radio = browser.find_element_by_css_selector("[for='robotsRule']")
    click_radio.click()

    click_button = browser.find_element_by_css_selector("[type='submit']")
    click_button.click()
finally:
    time.sleep(10)
    browser.quit()