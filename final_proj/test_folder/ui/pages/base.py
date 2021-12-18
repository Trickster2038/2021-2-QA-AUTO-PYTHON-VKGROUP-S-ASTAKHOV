from selenium import webdriver
from ui.locators.base_locators import BasePageLocators
from config import *

class BasePage:

    locators = BasePageLocators

    def __init__(self, driver):
        self.driver: webdriver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def exist(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def send_keys(self, locator, text):
        elem = self.find(locator)
        elem.clear()
        return elem.send_keys(text)

    def url_include(self, keyword):
        return self.driver.current_url.count(keyword) > 0

    def click(self, locator):
        return self.driver.find_element(*locator).click()

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def close_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.close()
