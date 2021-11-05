import pytest
from client import ApiClient 

@pytest.fixture(scope="function", autouse=True)
def client():
    client = ApiClient()
    client.login_simple()
    yield client