import pytest
from config import *
from api.api_client import ApiClient
from utils.fake_user import FakeUser
from orm.orm_client import MysqlORMClient
from orm.models import User
from ui.fixtures import *
from ui.pages.login_page import LoginPage
from utils.containers.infrastructure import Containers


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        Containers.setup()
        waiter = ApiClient(APP_HOST, APP_PORT,
                           API_CLIENT_USERNAME, API_CLIENT_PASSWORD)
        waiter.wait_app_up()

    client = MysqlORMClient(DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT)
    client.connect(db_created=True)

    if not hasattr(config, 'workerinput'):
        client.truncate_table()
        user = User(username=API_CLIENT_USERNAME,
                    email=API_CLIENT_EMAIL,
                    password=API_CLIENT_PASSWORD)
        client.session.add(user)
        client.session.commit()

    config.mysql_orm_client = client


def pytest_unconfigure(config):
    pass
    Containers.teardown()

    # client = config.mysql_orm_client
    # client.connect(db_created=True)
    # if not hasattr(config, 'workerinput'):
    #     client.truncate_table()
    #     pass


@pytest.fixture(scope="session", autouse=True)
def api_cli():
    client = ApiClient(APP_HOST, APP_PORT,
                       API_CLIENT_USERNAME, API_CLIENT_PASSWORD)
    yield client


@pytest.fixture(scope="function", autouse=True)
def login(api_cli):
    api_cli.post_login()


@pytest.fixture(scope="function", autouse=False)
def fake_person():
    yield FakeUser()


@pytest.fixture(scope="session", autouse=True)
def orm_cli(request):
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()


@pytest.fixture(scope='function', autouse=False)
def login_ui(driver):
    page = LoginPage(driver)
    page.go_to_this_page()
    page.login(API_CLIENT_USERNAME, API_CLIENT_PASSWORD)
    yield page
