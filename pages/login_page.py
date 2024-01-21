from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        """
        Verifies that the current page is the login page.
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Checks if 'login' is in the current URL.
        """
        assert "login" in self.browser.current_url, "Login is not present in URL"

    def should_be_login_form(self):
        """
        Verifies that the login form is present on the page.
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """
        Verifies that the registration form is present on the page.
        """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password):   
        """
        Registers a new user with the provided email and password.

        :param email: Email for the new user registration.
        :param password: Password for the new user registration.
        """
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        password_input.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD)
        confirm_password.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        submit_button.click()