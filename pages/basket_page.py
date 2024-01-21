from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket_text_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "There's no 'Your basket is empty' text"
        
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_ITEMS), "Basket contains some items, but should not"