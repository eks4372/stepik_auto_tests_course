from .pages.product_page import ShopPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


# def test_guest_can_go_to_login_page(browser):
#     page = ShopPage(browser, link)
#     page.open()


def test_guest_can_add_to_basket(browser):
    page = ShopPage(browser, link)
    page.open()
    page.add_to_basket()
    data = page.entering_in_basket()
    assert "The shellcoder's handbook" in data[0], 'купленной книги нет в корзине'
    assert '9.99' in data[1], 'не верн цена книги'