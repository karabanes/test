from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "C:/Users/111/test/3.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'form>input:nth-child(1)')
    input1.send_keys("Багдасарьян")
    input3 = browser.find_element(By.CSS_SELECTOR, 'form>input:nth-of-type(2)')
    input3.send_keys("Михаил")
    input4 = browser.find_element(By.CSS_SELECTOR, 'form>[name="middleName"]')
    input4.send_keys("Владиславович")
    input5 = browser.find_element(By.CLASS_NAME, 'email')
    input5.send_keys("sobaka@gmail.com")
    option = browser.find_element(By.CSS_SELECTOR, '[for="student"]')
    option.click()
    option1 = browser.find_element(By.CSS_SELECTOR, '[value="russian"]')
    option1.click() 
    option = browser.find_element(By.CSS_SELECTOR, '[value="english"]')
    option.click()
    option = browser.find_element(By.CSS_SELECTOR, '[value="other"]')
    option.click()
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()

    time.sleep(7)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла