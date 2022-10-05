from selenium.webdriver.common.by import By


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, '[name="login_submit"]')
    LOGIN_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')
