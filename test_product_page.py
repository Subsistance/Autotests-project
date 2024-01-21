from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
import pytest
import time


# def test_guest_cant_see_success_message(browser):
    # link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    # page = ProductPage(browser,link)
    # page.open()
    # page.should_not_be_success_message()
        
# def test_guest_can_add_product_to_basket(browser):
    # link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    # page = ProductPage(browser,link)
    # page.open()
    # page.add_to_basket()
    # page.parse_product_name()
    # page.parse_product_price()
    # page.verify_added_product_name()
 
# @pytest.mark.xfail 
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    # page = ProductPage(browser,link)
    # page.open()
    # page.add_to_basket()
    # page.should_not_be_success_message()

# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
    # link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    # page = ProductPage(browser,link)
    # page.open()
    # page.add_to_basket()
    # page.success_message_should_disappear()
    
# def test_guest_should_see_login_link_on_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.should_be_login_link()
    
# def test_guest_can_go_to_login_page_from_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # page = ProductPage(browser, link)
    # page.open()
    # page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()
    
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # link = "http://selenium1py.pythonanywhere.com"
    # page = BasePage(browser, link)
    # page.open()
    # page.go_to_basket_page()
    # basket_page = BasketPage(browser, browser.current_url)
    # basket_page.basket_should_be_empty()
    # basket_page.empty_basket_text_present()
    
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "test"
        
        page.register_new_user(email,password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self,browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
        
    def test_user_can_add_product_to_basket(self,browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.add_to_basket()
        page.parse_product_name()
        page.parse_product_price()
        page.verify_added_product_name()