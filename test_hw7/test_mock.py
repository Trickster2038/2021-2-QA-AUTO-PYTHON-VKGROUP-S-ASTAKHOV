# from conftest import clear_data, client
from mock.flask_mock import SURNAME_DATA
from client import ClientRequests
import pytest


@pytest.mark.mock
class TestMock:

    @pytest.fixture(autouse=True)
    def _clear_data(self):
        keys = list(SURNAME_DATA.keys())
        for key in keys:
            del SURNAME_DATA[key]
        yield

    def test_get_surname(self, first_name, last_name, client: ClientRequests):
        SURNAME_DATA[first_name] = last_name
        resp = client.get_surname(first_name)
        assert resp.status_code == 200
        assert str(resp.json()) == last_name

    def test_get_surname_negative(self, first_name, client: ClientRequests):
        resp = client.get_surname(first_name)
        assert resp.status_code == 404
        assert str(resp.json()) == f'Surname for user {first_name} not found'

    def test_update_surname(self, first_name, last_name, client: ClientRequests):
        SURNAME_DATA[first_name] = None
        resp = client.put_update_user(first_name, last_name)
        assert resp.status_code == 200
        assert SURNAME_DATA[first_name] == last_name

    def test_update_surname_negative(self, first_name, last_name, client: ClientRequests):
        resp = client.put_update_user(first_name, last_name)
        assert resp.status_code == 404
        assert str(resp.json()) == f'User {first_name} does not exist'

    def test_add_user(self, first_name, client: ClientRequests):
        resp = client.post_add_user(first_name)
        assert resp.status_code == 200
        assert str(resp.json()) == f'User {first_name} created'

    def test_add_user_negative(self, first_name, client: ClientRequests):
        SURNAME_DATA[first_name] = None
        resp = client.post_add_user(first_name)
        assert resp.status_code == 404
        assert str(resp.json()) == f'User {first_name} already exists'

    def test_delete_user(self, first_name, client: ClientRequests):
        SURNAME_DATA[first_name] = None
        resp = client.delete_user(first_name)
        assert resp.status_code == 200
        assert not (first_name in SURNAME_DATA)

    def test_delete_user_negative(self, first_name, client: ClientRequests):
        resp = client.delete_user(first_name)
        assert resp.status_code == 404
        assert str(resp.json()) == f'User {first_name} does not exist'
