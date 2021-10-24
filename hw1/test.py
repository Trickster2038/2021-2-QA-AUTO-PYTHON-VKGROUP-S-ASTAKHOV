from selenium import webdriver
import pytest
import locators
import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.UI
def test_login(browser):
    """
    Auth was made in fixture, just checking default page load
    """
    assert len(browser.find_elements(
        *locators.LOGIN_INSTRUCTIONS_LOCATOR)) != 0

# @pytest.mark.flacky


@pytest.mark.UI
def test_logout(browser):
    """
    1 - click on profile slider
    2 - click "logout"
    3 - check if "login" button appeared
    """

    # page reloads once before final rendering, so we need to wait for final rendering
    # before clickcking on slider
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(locators.LOGIN_INSTRUCTIONS_LOCATOR))
    slider = browser.find_element(*locators.PROFILE_SLIDER_LOCATOR)
    slider.click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(locators.LOGOUT_BTN_LOCATOR))
    logout = browser.find_element(*locators.LOGOUT_BTN_LOCATOR)
    logout.click()
    assert len(browser.find_elements(*locators.LOGIN_BTN_LOCATOR)) != 0

@pytest.mark.UI
def test_edit_contacts(browser, name, phone_num):
    """
    1 - get to profile tab
    2 - enter new name and phone
    3 - check notification
    4 - refresh
    5 - check new name in status bar
    """
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(locators.PROFILE_TAB_LOCATOR))

    tab = browser.find_element(*locators.PROFILE_TAB_LOCATOR)
    tab.click()

    fio = browser.find_element(*locators.FIO_FIELD_LOCATOR)
    fio.clear()
    fio.send_keys(name)

    phone = browser.find_element(*locators.PHONE_FIELD_LOCATOR)
    phone.clear()
    phone.send_keys(phone_num)

    save = browser.find_element(*locators.PROFILE_SAVE_BTN_LOCATOR)
    save.click()
    time.sleep(3)
    assert len(browser.find_elements(*locators.NOTIFICATION_LOCATOR)) != 0
    browser.refresh()
    fio_echo = browser.find_element(*locators.SLIDER_USERNAME_LOCATOR)
    assert fio_echo.text == name.upper()


@pytest.mark.UI
@pytest.mark.parametrize(
    'tab_locator, page_url',
    [
        pytest.param(locators.TAB_BILLING_LOCATOR,
                     'https://target.my.com/billing'),
        pytest.param(locators.TAB_STATS_LOCATOR,
                     'https://target.my.com/statistics')
    ]
)
def test_tabs_accessibility(browser, tab_locator, page_url):
    """
    1 - click on tab
    2 - check url
    """
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(tab_locator))

    tab = browser.find_element(*tab_locator)
    tab.click()
    assert browser.current_url.startswith(page_url)
