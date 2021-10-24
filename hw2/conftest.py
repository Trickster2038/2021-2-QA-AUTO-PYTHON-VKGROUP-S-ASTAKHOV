from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from ui.pages.basepage import BasePage

@pytest.fixture(scope='function', autouse=True)
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)
    browser.maximize_window()  # all tabs are on the screen
    yield browser
    browser.close()

@pytest.fixture(scope='function', autouse=False)
def login(browser):
    page = BasePage(browser)
    page.go_to_main()
    page.login("tttshelby6@gmail.com", "S3leniumpass")
    yield page

