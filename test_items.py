from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_present(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), 'нет кнопки "Добавить в корзину"'

# pytest --language=es test_items.py
