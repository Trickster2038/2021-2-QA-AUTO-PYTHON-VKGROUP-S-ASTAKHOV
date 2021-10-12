from selenium.webdriver.common.by import By

LOGIN_BTN_LOCATOR = (By.XPATH, "//div[starts-with(@class, 'responseHead-module-button')]")
EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[name="email"]')
PASSWORD_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[name="password"]')
LOGIN_FORM_BTN_LOCATOR = (By.XPATH, "//div[starts-with(@class, 'authForm-module-button')]")