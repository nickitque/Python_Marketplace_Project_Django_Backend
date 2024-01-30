import time
import pytest
from .pages.login_page import LoginPage

link = "http://127.0.0.1:8000/login/"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "Qq391609404"
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()


def test_guest_can_register_new_acc(browser):
    page = LoginPage(browser, link)
    page.open()
    page.login_user("nickitquee", "Sdsdwqe321")
    time.sleep(5)
