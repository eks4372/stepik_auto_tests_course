from .base_page import BasePage
from .locators import LoginPageLocators


link = "http://selenium1py.pythonanywhere.com/"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Registration link is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REG_EMAI_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_CONF).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_LINK).click()

