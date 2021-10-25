from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from ui.pages.basepage import BasePage
import logging
import allure
import os
import sys
import shutil

def pytest_addoption(parser):
    parser.addoption('--debug_log', action='store_true')

@pytest.fixture(scope='function', autouse=True)
def browser(logger):
    # logger.info("hello log")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    browser.maximize_window()  # all tabs are on the screen
    yield browser
    browser.close()

@pytest.fixture(scope='function', autouse=False)
def login(browser):
    page = BasePage(browser)
    page.go_to_main()
    page.login("tttshelby6@gmail.com", "S3leniumpass")
    yield page

# === temp dirs, allure and logs settings ===

@pytest.fixture(scope='session')
def config(request):
    debug_log = request.config.getoption('--debug_log')
    return {'debug_log': debug_log}

@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):  # in master only
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)

        os.makedirs(base_dir)

    config.base_temp_dir = base_dir  # everywhere


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir,
                            request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))