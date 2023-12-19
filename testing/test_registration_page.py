import time
import pytest
from .pages.login_page import RegistrationPage


link = "http://127.0.0.1:8000/signup/"


def test_guest_can_register_new_acc(browser):
    page = RegistrationPage(browser, link)
    page.open()
    page.register_new_user("nickitquee", str(time.time()) + "@fakemail.org", "Sdsdwqe321")
    time.sleep(5)
