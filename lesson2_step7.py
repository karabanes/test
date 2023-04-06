from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
import math



current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)
print(current_dir)
print(file_path)

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля
    span1 = browser.find_element(By.ID, 'input_value')
    span1 = span1.text

    value1=calc(span1) 
    print(value1)

    
    elements = browser.find_elements(By.ID, "answer")
    for element in elements:
        element.send_keys(value1)

    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    

    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    
                  

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    # Отправляем заполненную форму


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



