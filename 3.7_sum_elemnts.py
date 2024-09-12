from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/usr/local/bin/chromedriver'

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

url = 'https://parsinger.ru/selenium/7/7.html'

browser.get(url)
time.sleep(2)

select_element = browser.find_element(By.ID, 'opt')

select = Select(select_element)
total_sum = 0

for option in select.options:
    total_sum += int(option.text)

print("Сумма всех значений:", total_sum)

input_field = browser.find_element(By.ID, 'input_result')
input_field.send_keys(str(total_sum))

send_button = browser.find_element(By.ID, 'sendbutton')
browser.execute_script("arguments[0].removeAttribute('disabled')", send_button)

send_button.click()
time.sleep(2)
browser.quit()
