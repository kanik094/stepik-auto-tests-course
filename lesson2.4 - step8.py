from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    price = browser.find_element(By.ID, "price").text

    while True:
        if price == "$100":
            button_book = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "book")))
            button_book.click()
            break
        else:
            price = browser.find_element(By.ID, "price").text

    func = lambda v: str(math.log(abs(12 * math.sin(int(v)))))

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(func(x))

    button_submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    button_submit.click()

finally:
    browser.quit()




