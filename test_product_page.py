from .pages.product_page import ShopPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_can_add_to_basket(browser):
    page = ShopPage(browser, link)
    page.open()
    page.add_to_basket()
    data = page.entering_in_basket()
    assert data[2] in data[0], 'купленной книги нет в корзине'
    assert data[3] in data[1], 'не верн цена книги'