from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/usr/local/bin/chromedriver'

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

url = 'https://parsinger.ru/selenium/6/6.html'

browser.get(url)

time.sleep(2)
select_element = browser.find_element(By.ID, 'selectId')
select = Select(select_element)
select.select_by_visible_text('74604646177')

time.sleep(1)

send_button = browser.find_element(By.ID, 'sendbutton')
browser.execute_script("arguments[0].removeAttribute('disabled')", send_button)

send_button.click()

time.sleep(2)

browser.quit()
