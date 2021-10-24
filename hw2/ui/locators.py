from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_BTN = (By.XPATH, "//div[starts-with(@class, 'responseHead-module-button')]")
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_SUBMIT = (By.XPATH, "//div[starts-with(@class, 'authForm-module-button')]")
    