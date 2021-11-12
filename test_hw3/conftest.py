import pytest
from api.client import ApiClient
from api.credentials import Credentials


@pytest.fixture(scope="function", autouse=True)
def client():
    client = ApiClient()
    client.post_login(Credentials.LOGIN, Credentials.PASSWORD)
    yield client
