import pytest
from ui.locators import BasePageLocators


class BasePage:

    locators = BasePageLocators

    def __init__(self, driver):
        self.driver = driver

    def go_to_main(self):
        return self.driver.get("https://target.my.com")

    def go_to_campaign(self):
        return self.click(self.locators.TAB_CAMPAIGN)

    def login(self, username, password):
        login_btn = self.driver.find_element(*self.locators.LOGIN_BTN)
        login_btn.click()
        email_field = self.driver.find_element(*self.locators.EMAIL_FIELD)
        email_field.send_keys(username)
        pass_field = self.driver.find_element(*self.locators.PASSWORD_FIELD)
        pass_field.send_keys(password)
        submit_btn = self.driver.find_element(*self.locators.LOGIN_SUBMIT)
        submit_btn.click()

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def exist(self, locator):
        return len(self.driver.find_elements(*locator)) != 0

    def click(self, locator):
        return self.driver.find_element(*locator).click()

    def send_keys(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        return elem.send_keys(text)

    def send_file(self, locator, text):
        elem = self.find(locator)
        return elem.send_keys(text)