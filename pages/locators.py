from selenium.webdriver.common.by import By

    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-of-type(1) strong")
    PRODUCT_NAME = (By.XPATH, "//h1")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[contains(text(),'View basket')]")
    
class BasketPageLocators():
    EMPTY_BASKET = (By.XPATH, "//*[contains(text(),'Your basket is empty')]")
    BASKET_WITH_ITEMS = (By.CSS_SELECTOR, ".basket-items")