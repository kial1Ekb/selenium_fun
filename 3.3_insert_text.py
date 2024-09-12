from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/usr/local/bin/chromedriver'

service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)


def second(url):
    browser.get(url)
    time.sleep(2)
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    total_sum = 0

    for i in range(1, len(paragraphs), 2):
        try:
            value = int(paragraphs[i].text)
            total_sum += value
        except ValueError:
            print(f"Значение '{paragraphs[i].text}' не является числом и будет пропущено")
    print("Сумма значений каждого второго тега <p>:", total_sum)
    browser.quit()


second('https://parsinger.ru/selenium/3/3.html')
