from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/usr/local/bin/chromedriver'

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

url = 'https://parsinger.ru/selenium/2/2.html'

browser.get(url)

time.sleep(2)

try:
    link = browser.find_element(By.LINK_TEXT, '16243162441624')
    link.click()
except:
    print("Полное совпадение текста не найдено")

time.sleep(2)

current_url = browser.current_url
print("Текущий URL:", current_url)
