from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# link = "http://suninjuly.github.io/registration1.html"
def registration(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('Name')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('SecondName')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('ew@mail.tu')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return (welcome_text)
#
# # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# assert "Congratulations! You have successfully registered!" == welcome_text


# print(registration('http://suninjuly.github.io/registration1.html'))

