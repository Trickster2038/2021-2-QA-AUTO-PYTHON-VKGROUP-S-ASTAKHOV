from ui.pages.base import BasePage
from ui.locators.login_locators import LoginPageLocators
from config import *
import time
import allure
from allure_commons.types import AttachmentType


class LoginPage(BasePage):

    locators = LoginPageLocators
    url = f"http://{APP_HOST}:{APP_PORT}/"

    def go_to_this_page(self):
        return self.driver.get(self.url)

    def is_on_login_page(self):
        return self.driver.current_url.count('login') > 0

    def blocked_on_page(self):
        return self.driver.current_url == self.url

    @allure.step("login")
    def login(self, username, password):
        self.send_keys(self.locators.USERNAME, username)
        self.send_keys(self.locators.PASSWORD, password)
        self.click(self.locators.LOGIN_BTN)

    @allure.step("check notification")
    def notification_include(self, msg):
        i = 0
        while i < 10:
            elem = self.find(self.locators.NOTIFICATION)
            if len(elem.text) > 0:
                break
            time.sleep(0.1)
            i += 1
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="notification", attachment_type=AttachmentType.PNG)
        return elem.text.count(msg) > 0

    def notification_text_clear(self):
        i = 0
        while i < 10:
            elem = self.find(self.locators.NOTIFICATION)
            if len(elem.text) > 0:
                break
            time.sleep(0.1)
            i += 1
        fl = True
        symbols = ['%', '{', '}', '(', ')', '[', ']']
        for x in symbols:
            fl = fl and elem.text.count(x) == 0
        return fl
