from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def add_to_basket(self):
        """
        Clicks the 'Add to Basket' button.
        """
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()
        
    def parse_product_name(self):
        """
        Retrieves the product name from the product page.
        """
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name
        
    def parse_product_price(self):
        """
        Retrieves the product price from the product page.
        """
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price
        
    def verify_added_product_name(self):
        """
        Verifies that the product name in the alert matches the product name on the product page.
        """
        try:
            product_name = self.parse_product_name()
            alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
            assert product_name.text == alert_product_name.text, "Product name is different"
        except NoSuchElementException as e:
            raise AssertionError(f"Element not found: {e}")
            
    def verify_total_basket_price(self):
        """
        Verifies that the basket total matches the product price.
        """
        try:
            product_price = self.parse_product_price()
            basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
            assert basket_total.text == product_price.text, "Product price and basket total are different"
        except NoSuchElementException as e:
            raise AssertionError(f"Element not found: {e}")
        
    def should_not_be_success_message(self):
        """
        Asserts that a success message is not present on the product page.
        """
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def success_message_should_disappear(self):
        """
        Asserts that a success message disappears from the product page.
        """
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"