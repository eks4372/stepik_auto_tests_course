from selenium.webdriver.common.by import By


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.ID, 'login_link')
    REGISTRATION_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')
    REG_EMAI_INPUT = (By.ID, 'id_registration-email')
    REG_PASS_INPUT = (By.ID, 'id_registration-password1')
    REG_PASS_CONF = (By.ID, 'id_registration-password2')
    # REG_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ShoppingButtonBasket():
    BUTTON_LINK = (By.CLASS_NAME, 'btn-add-to-basket')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn-default')
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-4 a')
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-1 p')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_ITEM = (By.CLASS_NAME, 'basket-items')
    BASKET_INNER = (By.CSS_SELECTOR, '#content_inner a')


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
