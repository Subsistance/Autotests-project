from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
import pytest
import time


def test_guest_cant_see_success_message(browser):
    """
    Test to ensure a guest user does not see a success message 
    upon opening a product page without adding any products to the basket.
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
      
@pytest.mark.need_review      
def test_guest_can_add_product_to_basket(browser):
    """
    Test to ensure a guest user can add a product to the basket
    and verify the product name and price.
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.parse_product_name()
    page.parse_product_price()
    page.verify_added_product_name()
 
@pytest.mark.xfail 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Test to verify that a success message is not displayed to a guest user 
    after they add a product to the basket. Expected to fail (xfail).
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Test to verify that any success message shown after adding a product to the basket
    disappears after a certain period. Expected to fail (xfail).
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()
    
def test_guest_should_see_login_link_on_product_page(browser):
    """
    Test to ensure that a guest user can see a login link on the product page.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Test to ensure a guest user can navigate to the login page from the product page.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Test to verify that a guest user sees no products in the basket 
    when opened from the product page.
    """
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.empty_basket_text_present()
    
class TestUserAddToBasketFromProductPage():
    """
    Test cases for a user adding products to the basket from the product page.
    """
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Setup method to register a new user before each test.
        """
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "test"
        
        page.register_new_user(email,password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self,browser):
        """
        Test that verifies a user cannot see a success message after opening a product page.
        """
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        """
        Test that verifies a user can add a product to the basket and verify its name.
        """
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.add_to_basket()
        page.parse_product_name()
        page.parse_product_price()
        page.verify_added_product_name()