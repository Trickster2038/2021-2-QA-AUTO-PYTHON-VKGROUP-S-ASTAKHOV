from test_ui.base import BaseCase
import pytest
import time
from config import *
from ui.locators.main_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import allure


@allure.epic("UI")
@allure.feature("Main page")
@pytest.mark.UI
class TestMainPage(BaseCase):

    @pytest.fixture(scope='function', autouse=True)
    def login(self, login_ui):
        pass

    def test_logout(self):
        '''
        1 - Login (fixture)
        2 - Go to main page
        3 - Press logout key
        4 - Check that user thrown to login page
        '''
        self.main_page.go_to_this_page()
        self.main_page.logout_ui()
        assert self.login_page.is_on_login_page()

    @pytest.mark.parametrize("icon, keyword",
                             [
                                 (MainPageLocators.ICON_API, 'API'),
                                 (MainPageLocators.ICON_SMTP, 'SMTP'),
                                 #  (MainPageLocators.ICON_FUTURE,
                                 #   'future-of-the-internet')
                             ])
    def test_icons_links(self, icon, keyword):
        '''
        1 - Login (fixture)
        2 - Go to main page
        3 - Click on banner/icon
        4 - Switch to last tab
        5 - Check url
        6 - Check that new tab is opened
        '''
        n_tabs = len(self.driver.window_handles)
        self.main_page.go_to_this_page()
        self.main_page.click(icon)
        self.base_page.switch_to_last_tab()
        assert self.base_page.url_include(keyword)
        assert n_tabs + 1 == len(self.driver.window_handles)

    @pytest.mark.parametrize("tab, link_pairs",
                             [
                                 (MainPageLocators.TAB_PYTHON,
                                  [
                                      (MainPageLocators.LINK_FLASK, 'flask'),
                                  ]),
                                 (MainPageLocators.TAB_NETWORK,
                                  [
                                      (MainPageLocators.LINK_WIRESHARK_NEWS, 'news'),
                                      (MainPageLocators.LINK_WIRESHARK_DOWNLOAD,
                                       'download'),
                                      (MainPageLocators.LINK_EXAMPLES, 'examples')
                                  ]),
                                 pytest.param(MainPageLocators.TAB_PYTHON,
                                              [(
                                                  MainPageLocators.LINK_PYHTON_HISTORY, 'History_of_Python')
                                               ], marks=pytest.mark.xfail(reason="no new tab")),
                                 pytest.param(MainPageLocators.TAB_LINUX,
                                              [(
                                                  MainPageLocators.LINK_CENTOS, 'cent')
                                               ], marks=pytest.mark.xfail(reason="mismatched links"))
                             ])
    def test_tabs_valid(self, tab, link_pairs):
        '''
        1 - Login (fixture)
        2 - Go to main page
        3 - Move to top bar tab
        4 - Click to link in tab
        5 - Move to last tab
        6 - Check url
        7 - Check that new new tab is opened
        '''
        for pair in link_pairs:
            self.main_page.go_to_this_page()
            self.main_page.driver.refresh()
            elem = self.main_page.find(tab)
            hover = ActionChains(self.driver).move_to_element(elem)
            hover.perform()
            n_tabs = len(self.driver.window_handles)
            time.sleep(1)
            self.main_page.click(pair[0])
            self.base_page.switch_to_last_tab()
            assert self.base_page.url_include(pair[1])
            assert n_tabs + 1 == len(self.driver.window_handles)
            self.base_page.close_last_tab()
            self.base_page.switch_to_first_tab()

    @pytest.mark.parametrize("icon",
                             [
                                 (MainPageLocators.APP_ICON),
                                 (MainPageLocators.ICON_HOME)
                             ])
    def test_home_links(self, icon):
        '''
        1 - Login (fixture)
        2 - Click to home icon
        3 - Check url
        '''
        self.main_page.go_to_this_page()
        self.main_page.click(icon)
        assert self.base_page.url_include('welcome')
