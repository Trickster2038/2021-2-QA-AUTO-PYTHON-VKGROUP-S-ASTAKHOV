import pytest
from orm.client import MysqlORMClient
import pandas as pd
from credentials import Database


def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(
        user=Database.USER, password=Database.PASSWORD, db_name=Database.NAME)
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()
    mysql_orm_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.create_count_table()
        mysql_orm_client.create_typed_requests_table()
        mysql_orm_client.create_client_errors_requests_table()
        mysql_orm_client.create_frequent_requests_table()
        mysql_orm_client.create_frequent_users_table()
    config.mysql_orm_client = mysql_orm_client


@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MysqlORMClient:
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()


def pytest_addoption(parser):
    parser.addoption(
        "--logfile", action="store", default="access.log", help="log file name"
    )


@pytest.fixture(scope='session')
def logfile(request):
    return request.config.getoption("--logfile")


@pytest.fixture(scope='session')
def log_df(logfile):
    names = ["ip", "1", "2", "3", "4", "url", "status", "size", "5", "6", "7"]
    df = pd.read_csv(logfile, sep=" ", usecols=range(
        11), low_memory=False, header=None, names=names)
    df = df.iloc[:, [0, 5, 6, 7, 8, 9, 10]]
    yield df
