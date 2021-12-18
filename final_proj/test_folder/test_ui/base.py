from ui.pages.base import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.register_page import RegisterPage
from ui.pages.main_page import MainPage
import pytest
from _pytest.fixtures import FixtureRequest
from utils.fake_user import FakeUser
from selenium import webdriver
from api.mock_client import MockClient

class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, fake_person, request: FixtureRequest):
        self.driver: webdriver = driver
        self.fake_person: FakeUser = fake_person
        self.mock_cli: MockClient = request.getfixturevalue('mock_cli')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.register_page: RegisterPage = request.getfixturevalue('register_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.base_page: BasePage = request.getfixturevalue('base_page')