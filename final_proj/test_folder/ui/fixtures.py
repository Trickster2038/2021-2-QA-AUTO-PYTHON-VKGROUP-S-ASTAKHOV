from selenium import webdriver
import pytest
from ui.pages.login_page import LoginPage
from ui.pages.register_page import RegisterPage
from ui.pages.main_page import MainPage
from ui.pages.base import BasePage
from api.mock_client import MockClient
from config import *

@pytest.fixture(scope='function', autouse=False)
def driver():
    # browser = webdriver.Chrome(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    capabilities = {'browserName': 'chrome',
                    'version': '95.0',
                    'enableVNC': True,
                    'enableVideo': False,
                    # 'applicationContainers': ["app_docker:app_docker"]
                    # 'hostsEntries': ["127.0.0.1:127.0.0.1"]
                    }
    browser = webdriver.Remote(command_executor=f'http://{SELENOID_HOST}:{SELENOID_PORT}/wd/hub',
                               options=chrome_options, desired_capabilities=capabilities)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def register_page(driver):
    return RegisterPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def mock_cli():
    return MockClient(MOCK_HOST, MOCK_PORT, API_CLIENT_USERNAME, API_CLIENT_PASSWORD)
