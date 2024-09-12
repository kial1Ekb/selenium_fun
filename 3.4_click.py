from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/usr/local/bin/chromedriver'

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)

url = 'https://parsinger.ru/selenium/4/4.html'

browser.get(url)
time.sleep(2)

checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
time.sleep(2)

submit_button = browser.find_element(By.CLASS_NAME, 'btn')
submit_button.click()

time.sleep(15)
browser.quit()
