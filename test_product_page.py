from selenium.webdriver.common.by import By

from pages.product_page import ProductPage



import pytest
from pages.basket_page import BasketPage

from pages.test_login_page import LoginPage
from pages.main_page import MainPage
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019r"
    page=ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.xxx()
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019r"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019r"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.skip
def test_message_diappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019r"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_see_as_disappearing_message()   
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()    
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.no_goods()

    basket_page.basket_empty() 
@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page=LoginPage(browser,link)
        page.open()

        page.register_new_user("ddd@ya.ru","123456789@@")
        page.should_be_authorized_user() 
     
    def test_user_cant_see_success_message(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019r"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        #page.go_to_login_page()

        #login_page = LoginPage(browser, browser.current_url)

        #login_page.should_be_login_page()
 
    def test_user_can_add_product_to_basket(self,browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019r"
        page=ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.xxx() 