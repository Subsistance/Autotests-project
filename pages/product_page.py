from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()
        
    def parse_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name
        
    def parse_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price
        
    def verify_added_product_name(self):
        try:
            product_name = self.parse_product_name()
            alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
            assert product_name.text in alert_product_name.text, "Product name is different"
        except NoSuchElementException as e:
            raise AssertionError(f"Element not found: {e}")
            
    def verify_total_basket_price(self):
        try:
            product_price = self.parse_product_price()
            basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
            assert basket_total.text == product_price.text, "Product price and basket total are different"
        except NoSuchElementException as e:
            raise AssertionError(f"Element not found: {e}")