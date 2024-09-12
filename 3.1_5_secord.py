from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/usr/local/bin/chromedriver'

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

url = 'https://parsinger.ru/selenium/1/1.html'

browser.get(url)

browser.find_element(By.NAME, 'first_name').send_keys('Иван')
browser.find_element(By.NAME, 'last_name').send_keys('Иванов')
browser.find_element(By.NAME, 'patronymic').send_keys('Иванович')
browser.find_element(By.NAME, 'age').send_keys('30')
browser.find_element(By.NAME, 'city').send_keys('Москва')
browser.find_element(By.NAME, 'email').send_keys('ivanov@example.com')

browser.find_element(By.ID, 'btn').click()

time.sleep(2)

print("Форма успешно заполнена и отправлена.")
