from ui.pages.base import BasePage
from ui.locators.main_locators import MainPageLocators
from config import *
import allure

class MainPage(BasePage):

    url = f"http://{APP_HOST}:{APP_PORT}/welcome"
    url_logout = f"http://{APP_HOST}:{APP_PORT}/logout"
    locators = MainPageLocators

    def go_to_this_page(self):
        return self.driver.get(self.url)

    def is_on_main_page(self):
        return self.url.count('welcome') > 0

    @allure.step("logout with url")
    def logout(self):
        return self.driver.get(self.url_logout)

    @allure.step("logout with button")
    def logout_ui(self):
        self.click(self.locators.LOGOUT_BTN)