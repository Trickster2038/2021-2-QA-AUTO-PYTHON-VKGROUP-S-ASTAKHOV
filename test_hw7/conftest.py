import os
import signal
import subprocess
import time
from copy import copy

import requests
from requests.exceptions import ConnectionError
from requests.sessions import Session

import settings
import pytest
from client import ClientRequests

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

        ######### mock configuration #########
        from mock import flask_mock
        flask_mock.run_mock()

        wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)
        ######### mock configuration #########


def pytest_unconfigure(config):
    ######### mock unconfiguration #########
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')
    ######### mock configuration #########

@pytest.fixture(scope="session")
def client():
    url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'
    client = ClientRequests(url)
    yield client 