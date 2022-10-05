from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_present(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, '[value="Добавить в корзину"]'), 'нет кнопки "Добавить в корзину"'

# pytest --language=es test_items.py
