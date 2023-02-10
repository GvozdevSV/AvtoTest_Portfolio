# страница

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')
driver.maximize_window()
element = driver.find_element(By.CSS_SELECTOR, '#userName' )
element.send_keys('Иван')
email_element = driver.find_element(By.CSS_SELECTOR, '#userName' )
email_element.send_keys('Ivan1@yandex.ru')
address_element = driver.find_element(By.CSS_SELECTOR, '#currentAddress-wrapper > div:nth-child(2) > textarea:nth-child(1)' )
address_element.send_keys('Python – один из самых популярных языков для веб-автоматизации с Selenium, поскольку в нем есть упрощенный синтаксис, который позволяет выполнять больше задач за меньшее количество строк кода! Таким образом, Python и Selenium создают идеальную комбинацию для автоматизированного тестирования в вебе.')

button_element = driver.find_element(By.CSS_SELECTOR, '#submit' )
button_element.click()
time.sleep(5)