from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
   
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    print(new_window)
    '''confirm = browser.switch_to.alert
    confirm.accept()

    span1 = browser.find_element(By.ID, 'input_value')
    span1 = span1.text
    y = calc(int(span1))
    
    

    elements = browser.find_elements(By.ID, "answer")
    for element in elements:
        element.send_keys(y)
    

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
    time.sleep(3)'''


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()