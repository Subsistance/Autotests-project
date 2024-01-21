from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
import pytest
    
    
def test_should_see_login_form(browser):
    """
    Test to verify that the login form is present on the login page.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_should_see_register_form(browser):
    """
    Test to verify that the register form is present on the login page.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
    
def test_should_see_login_url(browser):
    """
    Test to verify that the current URL is the login URL.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Test to verify that a guest cannot see products in the basket when opened from the main page.
    """
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.empty_basket_text_present()
    
@pytest.mark.login_guest
class TestLoginFromMainPage():   
    """
    Tests to verify login functionality from the main page.
    """
    def test_guest_can_go_to_login_page(self, browser):
        """
        Test to verify that a guest can navigate to the login page.
        """
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """
        Test to verify that the login link is visible to a guest.
        """
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()