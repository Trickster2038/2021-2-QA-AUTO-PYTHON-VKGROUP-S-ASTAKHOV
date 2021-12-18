from selenium.webdriver.common.by import By
from ui.locators.login_locators import LoginPageLocators

class RegisterPageLocators(LoginPageLocators):
    EMAIL = (By.ID, 'email')
    CONFIRM_PASSWORD = (By.ID, 'confirm')
    TERM_CHECKBOX = (By.ID, 'term')
