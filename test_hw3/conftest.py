import pytest
from api.client import ApiClient
from api.credentials import Credentials
import os


@pytest.fixture(scope="function", autouse=True)
def client(media_root):
    client = ApiClient(media_root)
    client.post_login(Credentials.LOGIN, Credentials.PASSWORD)
    yield client

@pytest.fixture(scope='session')
def media_root():
    root =  os.path.abspath(os.path.join(__file__, os.path.pardir))
    return os.path.join(root, "media")