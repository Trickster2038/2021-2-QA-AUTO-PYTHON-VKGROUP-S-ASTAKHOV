from mock.flask_mock import SURNAME_DATA
from client import ClientRequests

def test_one(client:ClientRequests):
    SURNAME_DATA = {"Petr":"Ivanov"}
    client.get_surname("Petr")
    client.post_add_user("Ivan")
    client.post_add_user("Ivan")
    print(client.get_surname("Ivan").json())
    SURNAME_DATA['Ivan'] = "Qwerty"
    print(client.get_surname("Ivan").json())
    assert 1 == 1