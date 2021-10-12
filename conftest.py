from selenium import webdriver
import locators
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

@pytest.fixture(scope='function', autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(executable_path="./chromedriver", \
        options=chrome_options)
    try:
        browser.get("https://target.my.com")
        browser.implicitly_wait(10)
        login_btn = browser.find_element(*locators.LOGIN_BTN_LOCATOR)
        login_btn.click()
        email_field = browser.find_element(*locators.EMAIL_FIELD_LOCATOR)
        email_field.send_keys("tttshelby6@gmail.com")
        pass_field = browser.find_element(*locators.PASSWORD_FIELD_LOCATOR)
        pass_field.send_keys("S3leniumpass")
        login_btn = browser.find_element(*locators.LOGIN_FORM_BTN_LOCATOR)
        login_btn.click()
        yield browser
    finally:
        browser.close()