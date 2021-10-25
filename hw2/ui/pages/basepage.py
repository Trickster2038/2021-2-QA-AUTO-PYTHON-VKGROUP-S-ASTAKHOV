import pytest
from ui.locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging 
import allure


class BasePage:

    locators = BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')

    @allure.step("Open main page")
    def go_to_main(self):
        return self.driver.get("https://target.my.com")

    @allure.step("Open campaign page")
    def go_to_campaign(self):
        return self.click(self.locators.TAB_CAMPAIGN)

    @allure.step("Open segments page")
    def go_to_segments(self):
        return self.click(self.locators.TAB_SEGMENTS)
        
    @allure.step("Authentification")
    def login(self, username, password):
        self.logger.info(f"Authentification as {username}")
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
        self.logger.info(f"Click on {locator}")
        return self.driver.find_element(*locator).click()

    def send_keys(self, locator, text):
        self.logger.info(f"Send keys '{text}' to {locator}")
        elem = self.find(locator)
        elem.clear()
        return elem.send_keys(text)

    def send_file(self, locator, filepath):
        self.logger.info(f"Send file '{filepath}' to {locator}")
        elem = self.find(locator)
        return elem.send_keys(filepath)

    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))

    def wait_expired(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator))

    def is_displayed(self, locator):
        elem = self.find(locator)
        return elem.is_displayed()