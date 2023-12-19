from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://127.0.0.1:8000/login/"
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
