import pytest
from ui.locators import BasePageLocators


class BasePage:

    locators = BasePageLocators

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_btn = self.driver.find_element(*self.locators.LOGIN_BTN)
        login_btn.click()
        email_field = self.driver.find_element(*self.locators.EMAIL_FIELD)
        email_field.send_keys(username)
        pass_field = self.driver.find_element(*self.locators.PASSWORD_FIELD)
        pass_field.send_keys(password)
        submit_btn = self.driver.find_element(*self.locators.LOGIN_SUBMIT)
        submit_btn.click()
