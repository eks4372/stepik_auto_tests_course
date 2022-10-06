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
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-4 a')
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-1 p')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
