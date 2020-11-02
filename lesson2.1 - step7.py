from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/get_attribute.html"


try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    find_text_element = browser.find_element_by_id("treasure")
    x = find_text_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    input_text = browser.find_element_by_id("answer").send_keys(y)

    elements_to_select = ("[id='robotCheckbox']", "[id='robotsRule']", "[type='submit']",)
    for elem in elements_to_select:
        browser.find_element_by_css_selector(elem).click()




finally:
    time.sleep(10)
    browser.quit()