from .base_page import BasePage
from .locators import ShoppingButtonBasket


class ShopPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ShoppingButtonBasket.BUTTON_LINK)
        link.click()
        BasePage.solve_quiz_and_get_code(self)

    def entering_in_basket(self):
        self.browser.implicitly_wait(150)
        shop_name = self.browser.find_element(*ShoppingButtonBasket.BOOK_NAME).text
        shop_price = self.browser.find_element(*ShoppingButtonBasket.BOOK_PRICE).text
        basket = self.browser.find_element(*ShoppingButtonBasket.BASKET_LINK)
        basket.click()
        book_name = self.browser.find_element(*ShoppingButtonBasket.BOOK_NAME_IN_BASKET).text
        book_price = self.browser.find_element(*ShoppingButtonBasket.BOOK_PRICE_IN_BASKET).text
        return book_name, book_price, shop_name, shop_price
