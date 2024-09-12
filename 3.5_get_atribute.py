from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/usr/local/bin/chromedriver'

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

url = 'https://parsinger.ru/selenium/5/5.html'

browser.get(url)
time.sleep(2)
checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
for index, checkbox in enumerate(checkboxes):
    checkbox_type = checkbox.get_attribute('type')
    checkbox_class = checkbox.get_attribute('class')
    checkbox_value = checkbox.get_attribute('value')
    print(f"Чекбокс {index + 1}:")
    print(f"  type: {checkbox_type}")
    print(f"  class: {checkbox_class}")
    print(f"  value: {checkbox_value}")

browser.quit()
