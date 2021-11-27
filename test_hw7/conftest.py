import os
import time
from _pytest.fixtures import yield_fixture
from mock import flask_mock
from mock.flask_mock import SURNAME_DATA


import requests
from requests.exceptions import ConnectionError

import settings
import pytest
from client import ClientRequests
from faker import Faker

fake = Faker()

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 5s!')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        
        flask_mock.run_mock()

        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_unconfigure(config):
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')

@pytest.fixture(scope="session")
def client():
    url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'
    client = ClientRequests(url)
    yield client 

@pytest.fixture(scope="function", autouse=True)
def clear_data():
    keys = list(SURNAME_DATA.keys())
    for key in keys:
        del SURNAME_DATA[key]
    yield

@pytest.fixture
def first_name():
    yield fake.first_name()

@pytest.fixture
def last_name():
    yield fake.last_name()