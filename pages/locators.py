from selenium.webdriver.common.by import By


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, '[name="login_submit"]')
    LOGIN_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ShoppingButtonBasket():
    BUTTON_LINK = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_LINK = (By.CLASS_NAME, 'btn-cart')
    BOOK_NAME = (By.CLASS_NAME, 'col-sm-4')
    BOOK_PRICE = (By.CLASS_NAME, 'price_color')
