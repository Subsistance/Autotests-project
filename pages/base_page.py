from selenium.common.exceptions import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException
)
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        """
        Base class initialization.

        :param browser: Instance of the browser (WebDriver).
        :param url: URL to open in the browser.
        :param timeout: Time to wait for an element to appear.
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        """
        Opens the URL in the browser.
        """
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        """
        Checks if an element is present on the page.

        :param how: By method to locate the element (e.g., By.ID, By.CSS_SELECTOR).
        :param what: The locator string.
        :return: True if element is present, False otherwise.
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        
    def go_to_login_page(self):
        """
        Navigates to the login page.
        """
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        """
        Verifies that a login link is present on the page.
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        
    def go_to_basket_page(self):
        """
        Navigates to the basket page.
        """
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()
        
    def solve_quiz_and_get_code(self):
        """
        Solves the quiz in an alert and retrieves the code if present.
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # commented for the case when second alert is not present
        # try:
            # alert = self.browser.switch_to.alert
            # alert_text = alert.text
            # print(f"Your code: {alert_text}")
            # alert.accept()
        # except NoAlertPresentException:
            # print("No second alert presented")
            
    def is_not_element_present(self, how, what, timeout=4):
        """
        Checks if an element is not present on the page.

        :param how: By method to locate the element.
        :param what: The locator string.
        :param timeout: Time to wait for the element's presence.
        :return: True if element is not present within timeout, False otherwise.
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
        
    def is_disappeared(self, how, what, timeout=4):
        """
        Checks if an element disappears from the page.

        :param how: By method to locate the element.
        :param what: The locator string.
        :param timeout: Time to wait for the element to disappear.
        :return: True if the element disappears, False otherwise.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
        
    def should_be_authorized_user(self):
        """
        Verifies that the user icon is present on the page, indicating authorized user.
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"