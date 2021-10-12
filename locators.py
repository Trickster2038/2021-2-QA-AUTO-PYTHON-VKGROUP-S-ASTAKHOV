from selenium.webdriver.common.by import By

LOGIN_BTN_LOCATOR = (By.XPATH, "//div[starts-with(@class, 'responseHead-module-button')]")
EMAIL_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[name="email"]')
PASSWORD_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[name="password"]')
LOGIN_FORM_BTN_LOCATOR = (By.XPATH, "//div[starts-with(@class, 'authForm-module-button')]")

LOGIN_INSTRUCTIONS_LOCATOR = (By.XPATH, "//div[starts-with(@class, 'instruction-module-container')]")

PROFILE_SLIDER_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-mail')]")
LOGOUT_BTN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/logout"]')
MAINPAGE_BANNER_LOCATOR = (By.XPATH, "//div[starts-with(@class, 'mainPage-module-helloVKContent')]")

PROFILE_TAB_LOCATOR = (By.CSS_SELECTOR, 'a[href="/profile"]')
FIO_FIELD_LOCATOR = (By.CSS_SELECTOR, 'div[data-name="fio"] > * > input')
PROFILE_SAVE_BTN_LOCATOR = (By.CLASS_NAME, 'button_submit')
NOTIFICATION_LOCATOR = (By.CLASS_NAME, 'js-notification-content')
SLIDER_USERNAME_LOCATOR = (By.XPATH, "//div[starts-with(@class, 'right-module-userNameWrap')]")

# right-module-userNameWrap