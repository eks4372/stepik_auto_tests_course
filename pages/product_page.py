from .base_page import BasePage
from .locators import ShoppingButtonBasket
from .locators import ProductPageLocators



class ShopPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ShoppingButtonBasket.BUTTON_LINK)
        link.click()
        BasePage.solve_quiz_and_get_code(self)

    def review_basket(self):
        basket = self.browser.find_element(*ShoppingButtonBasket.BASKET_LINK)
        basket.click()
        assert not self.is_element_present(*ShoppingButtonBasket.BASKET_ITEM), 'В корзине что-то есть'
        assert self.browser.find_element(*ShoppingButtonBasket.BASKET_INNER).text is not None, 'В корзине что-то есть'

    def entering_in_basket(self):
        self.browser.implicitly_wait(150)
        shop_name = self.browser.find_element(*ShoppingButtonBasket.BOOK_NAME).text
        shop_price = self.browser.find_element(*ShoppingButtonBasket.BOOK_PRICE).text
        basket = self.browser.find_element(*ShoppingButtonBasket.BASKET_LINK)
        basket.click()
        book_name = self.browser.find_element(*ShoppingButtonBasket.BOOK_NAME_IN_BASKET).text
        book_price = self.browser.find_element(*ShoppingButtonBasket.BOOK_PRICE_IN_BASKET).text
        # return book_name, book_price, shop_name, shop_price
        assert book_name == shop_name, 'купленной книги нет в корзине'
        assert book_price == shop_price, 'не верная цена книги'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

