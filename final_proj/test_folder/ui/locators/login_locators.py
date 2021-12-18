from selenium.webdriver.common.by import By
from ui.locators.base_locators import BasePageLocators

class LoginPageLocators(BasePageLocators):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'submit')
    NOTIFICATION = (By.ID, 'flash')
