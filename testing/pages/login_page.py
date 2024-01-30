from .base_page import BasePage
from .locators import LoginPageLocators, RegistrationPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://127.0.0.1:8000/login/"
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def login_user(self, name, password):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(name)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BTN).click()
        assert self.browser.current_url == "http://127.0.0.1:8000/"


class RegistrationPage(BasePage):

    def should_be_login_page(self):
        self.should_be_signup_url()
        self.should_be_signup_form()

    def should_be_signup_url(self):
        assert self.browser.current_url == "http://127.0.0.1:8000/signup/"
        assert "signup" in self.browser.current_url

    def should_be_signup_form(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTRATION_FORM), "Signup form is not presented"

    def register_new_user(self, name, email, password):
        self.browser.find_element(*RegistrationPageLocators.USERNAME_FIELD).send_keys(name)
        self.browser.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.PASSWORD_FIELD_REPEAT).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.SUBMIT_BTN).click()
