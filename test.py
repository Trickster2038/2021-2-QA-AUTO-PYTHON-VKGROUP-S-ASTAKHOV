from selenium import webdriver
import pytest
import time
import conftest
import locators
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.UI
@pytest.mark.skip("SKIP")
def test_login(browser):
    assert len(browser.find_elements(*locators.LOGIN_INSTRUCTIONS_LOCATOR)) != 0

@pytest.mark.UI
@pytest.mark.skip("SKIP")
def test_logout(browser):
    element_present = EC.presence_of_element_located(locators.LOGIN_INSTRUCTIONS_LOCATOR)
    WebDriverWait(browser, 10).until(element_present)
    slider = browser.find_element(*locators.PROFILE_SLIDER_LOCATOR)
    slider.click()

    element_present = EC.element_to_be_clickable(locators.LOGOUT_BTN_LOCATOR)
    WebDriverWait(browser, 10).until(element_present)
    logout = browser.find_element(*locators.LOGOUT_BTN_LOCATOR)
    logout.click()
    assert len(browser.find_elements(*locators.LOGIN_BTN_LOCATOR)) != 0

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

