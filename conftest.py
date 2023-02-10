# файл используется для написания фикстур для каждого теста

import pytest
from selenium import webdriver

@pytest.fixture() #позволяет выполнять что-то до теста и после теста
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
