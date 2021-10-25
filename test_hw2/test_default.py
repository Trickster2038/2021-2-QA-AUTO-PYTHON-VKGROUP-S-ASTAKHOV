from ui.pages.basepage import BasePage
from ui.pages.campaignpage import CampaignPage
from ui.pages.segmentspage import SegmentPage
import time
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.locators import BasePageLocators
import pytest

from ui.pages.segmentspage import SegmentPage
from allure_commons.types import AttachmentType


@allure.epic("UI")
@allure.feature("login")
@allure.story("bad login")
@pytest.mark.UI
def test_auth_bad_login_format(browser: WebDriver):
    page = BasePage(browser)
    page.go_to_main()
    page.login("aaa", "bbb")
    assert page.exist(BasePageLocators.UNSUPPORTED_LOGIN_NOTICE)

    # extremely needed to finish animation, EC waiters doesn't help
    time.sleep(0.5)
    allure.attach(browser.get_screenshot_as_png(),
                  name="Login_notice", attachment_type=AttachmentType.PNG)


@allure.epic("UI")
@allure.feature("login")
@allure.story("bad password")
@pytest.mark.UI
def test_auth_bad_password(browser: WebDriver):
    page = BasePage(browser)
    page.go_to_main()
    page.login("123@gmail.com", "bbb")
    assert browser.current_url.count("login/?error_code=1") != 0


@allure.epic("UI")
@allure.feature("campaigns")
@allure.story("create campaign")
@pytest.mark.UI
def test_create_campaign(browser: WebDriver, login):
    cmpg_page = CampaignPage(browser)
    cmpg_page.go_to_campaign()
    name = cmpg_page.create_campaign_default()
    assert cmpg_page.campaign_exist(name)


@allure.epic("UI")
@allure.feature("segments")
@allure.story("create segment")
@pytest.mark.UI
def test_create_segment(browser: WebDriver, login):
    seg_page = SegmentPage(browser)
    seg_page.go_to_segments()
    name = seg_page.create_segment_default()
    assert seg_page.segment_exist(name)


@allure.epic("UI")
@allure.feature("segments")
@allure.story("delete segment")
@pytest.mark.UI
def test_delete_segment(browser: WebDriver, login):
    seg_page = SegmentPage(browser)
    seg_page.go_to_segments()
    name = seg_page.create_segment_default()
    assert seg_page.segment_exist(name)
    allure.attach(browser.get_screenshot_as_png(),
                  name="Segments_list_before_del", attachment_type=AttachmentType.PNG)
    seg_page.delete_segment(name)
    assert not seg_page.segment_exist(name)
    allure.attach(browser.get_screenshot_as_png(),
                  name="Segments_list_after_del", attachment_type=AttachmentType.PNG)
