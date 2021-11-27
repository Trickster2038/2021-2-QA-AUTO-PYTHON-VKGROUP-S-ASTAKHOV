from mock.flask_mock import SURNAME_DATA
from client import ClientRequests

def test_get_surname(first_name, last_name, client: ClientRequests):
    SURNAME_DATA[first_name] = last_name
    resp = client.get_surname(first_name)
    assert resp.status_code == 200
    assert str(resp.json()) == last_name

def test_get_surname_negative(client: ClientRequests):
    resp = client.get_surname('Pavel')
    assert resp.status_code == 404
    assert str(resp.json()) == 'Surname for user "Pavel" not found' 

def test_update_surname(client: ClientRequests):
    pass
