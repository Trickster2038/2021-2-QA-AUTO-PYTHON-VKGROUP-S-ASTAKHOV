import pytest
from api.client import ApiClient
from api.credentials import Credentials


@pytest.fixture(scope="function", autouse=True)
def client():
    client = ApiClient()
    client.login(Credentials.LOGIN, Credentials.PASSWORD)
    yield client
