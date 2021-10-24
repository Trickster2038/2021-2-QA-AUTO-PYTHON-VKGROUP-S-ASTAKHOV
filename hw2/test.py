from ui.pages.mainpage import MainPage
import time
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.locators import BasePageLocators
import pytest

@pytest.mark.skip
@pytest.mark.UI
def test_auth_bad_login_format(browser: WebDriver):
    page = MainPage(browser)
    page.go_to_page()
    page.login("aaa", "bbb")
    assert page.exist(BasePageLocators.UNSUPPORTED_LOGIN_NOTICE)

@pytest.mark.skip
@pytest.mark.UI
def test_auth_bad_password(browser: WebDriver):
    page = MainPage(browser)
    page.go_to_page()
    page.login("123@gmail.com", "bbb")
    assert browser.current_url.count("login/?error_code=1") != 0









