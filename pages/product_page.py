from .base_page import BasePage
from .locators import ShoppingButtonBasket


class ShopPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ShoppingButtonBasket.BUTTON_LINK)
        link.click()
        BasePage.solve_quiz_and_get_code(self)

    def entering_in_basket(self):
        self.browser.implicitly_wait(15)
        basket = self.browser.find_element(*ShoppingButtonBasket.BASKET_LINK)
        basket.click()
        book_name = self.browser.find_element(*ShoppingButtonBasket.BOOK_NAME).text
        book_price = self.browser.find_element(*ShoppingButtonBasket.BOOK_PRICE).text
        return book_name, book_price
