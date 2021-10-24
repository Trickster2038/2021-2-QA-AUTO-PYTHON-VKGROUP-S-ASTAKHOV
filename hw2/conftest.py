from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope='function', autouse=True)
def browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)
    browser.maximize_window()  # all tabs are on the screen
    yield browser
    browser.close()