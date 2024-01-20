from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import pytest

                             
# def test_guest_can_add_product_to_basket(browser):
    # link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    # page = ProductPage(browser,link)
    # page.open()
    # page.add_to_basket()
    # page.parse_product_name()
    # page.parse_product_price()
    # page.verify_added_product_name()
 
@pytest.mark.xfail 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()