from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()
        
    def verify_added_product_name(self):
        try:
            product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
            alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
            assert product_name.text in alert_product_name.text, "Product name is different"
        except NoSuchElementException as e:
            raise AssertionError(f"Element not found: {e}")
            
    def verify_total_basket_price(self):
        try:
            product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
            basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
            assert basket_total.text == product_price.text, "Product price and basket total are different"
        except NoSuchElementException as e:
            raise AssertionError(f"Element not found: {e}")