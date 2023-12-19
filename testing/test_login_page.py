import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Qq391609404"
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
        product_page.open()
        product_page.should_not_be_success_message_present()
