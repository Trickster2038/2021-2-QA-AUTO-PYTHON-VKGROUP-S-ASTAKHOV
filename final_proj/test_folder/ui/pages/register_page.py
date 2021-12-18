from ui.pages.login_page import LoginPage
from ui.locators.register_locators import RegisterPageLocators
from config import *
import allure

class RegisterPage(LoginPage):

    locators = RegisterPageLocators
    url = f"http://{APP_HOST}:{APP_PORT}/reg"

    @allure.step("register")
    def register(self, username, email, password, confirm, accept_box):
        self.send_keys(self.locators.EMAIL, email)
        self.send_keys(self.locators.CONFIRM_PASSWORD, confirm)
        if accept_box:
            self.click(self.locators.TERM_CHECKBOX)
        self.send_keys(self.locators.USERNAME, username)
        self.send_keys(self.locators.PASSWORD, password)
        self.click(self.locators.LOGIN_BTN)
