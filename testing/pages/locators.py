from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_btn_header")
    SIGNUP_LINK = (By.ID, "signup_btn_header")
    CALENDAR_LINK = (By.ID, "calendar_btn_header")
    MARKETPLACE_LINK = (By.ID, "marketplace_btn_header")
    USER_DASHBOARD_BTN = (By.ID, "dashboard_btn_header")
    USER_MSGS_BTN = (By.ID, "messages_btn_header")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    USERNAME_FIELD = (By.ID, "id_username")
    PASSWORD_FIELD = (By.ID, "id_password")
    SUBMIT_BTN = (By.ID, "submit_btn")
    LOGIN_FORM = (By.ID, "login_form")


class RegistrationPageLocators:
    USERNAME_FIELD = (By.ID, "id_username")
    EMAIL_FIELD = (By.ID, "id_email")
    PASSWORD_FIELD = (By.ID, "id_password1")
    PASSWORD_FIELD_REPEAT = (By.ID, "id_password2")
    SUBMIT_BTN = (By.ID, "submit_btn")
    REGISTRATION_FORM = (By.ID, "registration_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")
    ALERT_INNER_DISCOUNT = (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div")
    SUCCESS_MASSAGE_LINK = (By.CSS_SELECTOR, ".alert-success")
