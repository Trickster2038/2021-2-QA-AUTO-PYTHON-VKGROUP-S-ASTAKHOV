from ui.pages.basepage import BasePage
from ui.pages.campaignpage import CampaignPage
import time
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.locators import BasePageLocators, CampaignPageLocators
import pytest

@pytest.mark.skip
@pytest.mark.UI
def test_auth_bad_login_format(browser: WebDriver):
    page = BasePage(browser)
    page.go_to_main()
    page.login("aaa", "bbb")
    assert page.exist(BasePageLocators.UNSUPPORTED_LOGIN_NOTICE)

@pytest.mark.skip
@pytest.mark.UI
def test_auth_bad_password(browser: WebDriver):
    page = BasePage(browser)
    page.go_to_main()
    page.login("123@gmail.com", "bbb")
    assert browser.current_url.count("login/?error_code=1") != 0

@pytest.mark.UI
def test_create_campaign(browser: WebDriver, login):
    cmpg_page = CampaignPage(browser)
    cmpg_page.go_to_campaign()
    cmpg_page.create_campaign_default()
    assert cmpg_page.last_campaign_added()







