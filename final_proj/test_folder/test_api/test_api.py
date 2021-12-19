import pytest
from orm.models import User
from orm.orm_client import MysqlORMClient
from api.api_client import ApiClient
import allure

@allure.epic("API")
@allure.feature("app")
@allure.story("app status")
@pytest.mark.API
def test_app_status(api_cli: ApiClient):
    '''
    checking UP status
    '''
    resp = api_cli.get_app_status()    
    assert resp.status_code == 200
    assert resp.json()['status'] == 'ok'

@allure.epic("API")
@allure.feature("add user")
@allure.story("regular user")
@pytest.mark.API
def test_add_user(fake_person, api_cli, orm_cli: MysqlORMClient):
    '''
    1 - Count users
    2 - Add valid user
    3 - Check response OK code
    4 - Recount & compare users (must diff by 1)
    '''
    n_before_add = orm_cli.count(User)
    resp = api_cli.post_create_user(fake_person)
    assert resp.status_code == 210
    assert n_before_add + 1 == orm_cli.count(User)

@allure.epic("API")
@allure.feature("add user")
@allure.story("invalid data")

@pytest.mark.API
# @pytest.mark.xfail(reason="no validation - email")
def test_add_user_invalid_email(fake_person, api_cli, orm_cli: MysqlORMClient):
    '''
    1 - Count users
    2 - Add invalid user (email format)
    3 - Check response NOT OK code
    4 - Recount & compare users (must equal)
    '''
    n_before_add = orm_cli.count(User)
    fake_person.email = fake_person.username + '~gmail.com'
    resp = api_cli.post_create_user(fake_person)
    assert resp.status_code != 210
    assert n_before_add == orm_cli.count(User)

@allure.epic("API")
@allure.feature("add user")
@allure.story("invalid data")
# @pytest.mark.xfail(reason="no validation - password")
@pytest.mark.API
def test_add_user_empty_password(fake_person, api_cli, orm_cli: MysqlORMClient):
    '''
    1 - Count users
    2 - Add invalid user (empty password)
    3 - Check response NOT OK code
    4 - Recount & compare users (must equal)
    '''
    n_before_add = orm_cli.count(User)
    fake_person.password = ''
    resp = api_cli.post_create_user(fake_person)
    assert resp.status_code != 210
    assert n_before_add == orm_cli.count(User)

@allure.epic("API")
@allure.feature("add user")
@allure.story("invalid data")
# @pytest.mark.xfail(reason="no validation - username")
@pytest.mark.API
def test_add_user_empty_username(fake_person, api_cli, orm_cli: MysqlORMClient):
    '''
    1 - Count users
    2 - Add invalid user (empty usrname)
    3 - Check response NOT OK code
    4 - Recount & compare users (must equal)
    '''
    n_before_add = orm_cli.count(User)
    fake_person.username = ''
    resp = api_cli.post_create_user(fake_person)
    assert resp.status_code != 210
    assert n_before_add == orm_cli.count(User)

@allure.epic("API")
@allure.feature("add user")
@allure.story("invalid data")
# @pytest.mark.xfail(reason="no validation - email")
@pytest.mark.API
def test_add_existing_email_user(fake_person, api_cli, orm_cli: MysqlORMClient):
    '''
    1 - Count users
    2 - Add valid user
    3 - Try to add user with same email
    4 - Check response NOT OK code
    4 - Recount & compare users (must equal)
    '''
    api_cli.post_create_user(fake_person)
    fake_person.username = fake_person.username + 'aaa'
    n_before_add = orm_cli.count(User)
    resp = api_cli.post_create_user(fake_person)
    assert resp.status_code != 210
    assert n_before_add == orm_cli.count(User)

@allure.epic("API")
@allure.feature("add user")
@allure.story("invalid data")
@pytest.mark.API
def test_add_existing_login_user(fake_person, api_cli, orm_cli: MysqlORMClient):
    '''
    1 - Count users
    2 - Add valid user
    3 - Try to add user with same username
    4 - Check response has 'already exist'(304) code
    5 - Recount & compare users (must equal)
    '''
    api_cli.post_create_user(fake_person)
    fake_person.email = 'aaa' + fake_person.email
    n_before_add = orm_cli.count(User)
    resp = api_cli.post_create_user(fake_person)
    assert resp.status_code == 304
    assert n_before_add == orm_cli.count(User)

@allure.epic("API")
@allure.feature("delete user")
@pytest.mark.API
def test_delete_user(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Add user
    2 - Count users
    3 - Delete user
    4 - Check reponse 'deleted'(204) status code
    5 - Recount & compare users
    '''
    api_cli.post_create_user(fake_person)
    n_before_delete = orm_cli.count(User)
    resp = api_cli.get_delete_user(fake_person)
    assert resp.status_code == 204
    assert n_before_delete - 1 == orm_cli.count(User)

@allure.epic("API")
@allure.feature("delete user")
@pytest.mark.API
def test_delete_user_negative(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Try to delete not existing user
    2 - Check reponse 'not found'(404) status code
    '''
    resp = api_cli.get_delete_user(fake_person)
    assert resp.status_code == 404

@allure.epic("API")
@allure.feature("block user")
@pytest.mark.API
def test_block_user(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Create user
    2 - Block user
    3 - Check response 'ok'(200) code
    4 - Check that user is blocked
    '''
    api_cli.post_create_user(fake_person)
    resp = api_cli.get_block_user(fake_person)
    assert resp.status_code == 200
    assert orm_cli.get_access(fake_person) == 0

@allure.epic("API")
@allure.feature("block user")
@pytest.mark.API
def test_block_user_twice(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Create user
    2 - Block user
    3 - Try to block user 2nd time
    4 - Check response 'no changes'(304) code
    '''
    api_cli.post_create_user(fake_person)
    api_cli.get_block_user(fake_person)
    resp = api_cli.get_block_user(fake_person)
    assert resp.status_code == 304

@allure.epic("API")
@allure.feature("block user")
@pytest.mark.API
def test_block_user_negative(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Try to block not existing user
    2 - Check response 'not found'(404) code
    '''
    resp = api_cli.get_block_user(fake_person)
    assert resp.status_code == 404

@allure.epic("API")
@allure.feature("accept user")
@pytest.mark.API
def test_accept_user(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Create user
    2 - Block user
    3 - Accept user
    4 - Check response 'ok'(200) code
    5 - Check user have access
    '''
    api_cli.post_create_user(fake_person)
    api_cli.get_block_user(fake_person)
    resp = api_cli.get_accept_user(fake_person)
    assert resp.status_code == 200
    assert orm_cli.get_access(fake_person) == 1

@allure.epic("API")
@allure.feature("accept user")
@pytest.mark.API
def test_accept_user_twice(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Create user
    3 - Accept user twice
    4 - Check response 'no changes'(304) code
    '''
    api_cli.post_create_user(fake_person)
    api_cli.get_accept_user(fake_person)
    resp = api_cli.get_accept_user(fake_person)
    assert resp.status_code == 304

@allure.epic("API")
@allure.feature("accept user")
@pytest.mark.API
def test_accept_user_negative(fake_person, api_cli: ApiClient, orm_cli: MysqlORMClient):
    '''
    1 - Accept non existing user
    2 - Check response 'not found'(404) code
    '''
    resp = api_cli.get_accept_user(fake_person)
    assert resp.status_code == 404