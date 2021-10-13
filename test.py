from selenium import webdriver
import pytest
import locators
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Auth was made in fixture, just checking default page load
"""
@pytest.mark.UI
def test_login(browser):
    assert len(browser.find_elements(*locators.LOGIN_INSTRUCTIONS_LOCATOR)) != 0

"""
1 - click on profile slider
2 - click "logout"
3 - check if "login" button appeared
"""
@pytest.mark.UI
def test_logout(browser):
    element_present = EC.presence_of_element_located(locators.LOGIN_INSTRUCTIONS_LOCATOR)
    WebDriverWait(browser, 10).until(element_present)
    slider = browser.find_element(*locators.PROFILE_SLIDER_LOCATOR)
    slider.click()

    element_present = EC.presence_of_element_located(locators.LOGOUT_BTN_LOCATOR)
    WebDriverWait(browser, 10).until(element_present)
    logout = browser.find_element(*locators.LOGOUT_BTN_LOCATOR)
    element_clickable = EC.element_to_be_clickable(locators.LOGOUT_BTN_LOCATOR)
    WebDriverWait(browser, 10).until(element_clickable)
    logout.click()
    assert len(browser.find_elements(*locators.LOGIN_BTN_LOCATOR)) != 0

"""
1 - get to profile tab
2 - enter new name
3 - check notification
4 - refresh
5 - check new name in status bar
"""
@pytest.mark.UI
def test_edit(browser):
    element_present = EC.presence_of_element_located(locators.PROFILE_TAB_LOCATOR)
    WebDriverWait(browser, 10).until(element_present)

    tab = browser.find_element(*locators.PROFILE_TAB_LOCATOR)
    tab.click()
    fio = browser.find_element(*locators.FIO_FIELD_LOCATOR)
    name = random.choice(["abcd", "123", "Ivan Ivanov", "Qwerty"])
    fio.clear()
    fio.send_keys(name)
    save = browser.find_element(*locators.PROFILE_SAVE_BTN_LOCATOR)
    save.click()
    assert len(browser.find_elements(*locators.NOTIFICATION_LOCATOR)) != 0
    browser.refresh()
    fio_echo = browser.find_element(*locators.SLIDER_USERNAME_LOCATOR)
    assert fio_echo.text == name.upper()

"""
1 - click on tab
2 - check url
"""
@pytest.mark.UI
@pytest.mark.parametrize(
        'tab_locator, page_url',
        [
            pytest.param(locators.TAB_BILLING_LOCATOR, 'https://target.my.com/billing'),
            pytest.param(locators.TAB_STATS_LOCATOR, 'https://target.my.com/statistics')
        ]
    )
def test_tabs(browser, tab_locator, page_url):
    element_present = EC.presence_of_element_located(tab_locator)
    WebDriverWait(browser, 10).until(element_present)

    tab = browser.find_element(*tab_locator)
    tab.click()
    assert browser.current_url.startswith(page_url)
