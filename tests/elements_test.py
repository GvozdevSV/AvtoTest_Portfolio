import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://habr.com/ru/post/549450/')
    page.open()
    time.sleep(2)
