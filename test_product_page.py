import time

from .pages.product_page import ShopPage
import pytest


# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_to_basket(browser, link):
    page = ShopPage(browser, link)
    page.open()
    page.add_to_basket()
    time.sleep(150)
    data = page.entering_in_basket()
    assert data[2] == data[0], 'купленной книги нет в корзине'
    assert data[3] == data[1], 'не верная цена книги'


@pytest.mark.parametrize('link',
                         ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ShopPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link',
                         ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'])
def test_guest_cant_see_success_message(browser, link):
    page = ShopPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link',
                         ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ShopPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ShopPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ShopPage(browser, link)
    page.open()
    page.go_to_login_page()
