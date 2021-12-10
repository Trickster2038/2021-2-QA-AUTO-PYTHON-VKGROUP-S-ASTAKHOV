from pandas.core.base import DataError
from sqlalchemy import func
from sqlalchemy.sql.functions import count

from orm.models import CountRequests, FrequentRequests, FrequentUsers, TypedRequests, ClientErrosRequests
from test_orm.base import MysqlBase
import pandas as pd
import pytest
from utils import datahandler


@pytest.mark.ORM
class TestMysqlLogSaving(MysqlBase):

    def test_requests_count(self, log_df):
        self.mysql.insert_count_requests(log_df)
        assert self.mysql.session.query(CountRequests).count() == 1

    def test_requests_by_type(self, log_df):
        df = datahandler.get_requests_by_type(log_df)
        self.mysql.insert_typed_requests(df)
        assert self.mysql.session.query(TypedRequests).count() == df.shape[0]

    def test_frequent_requests(self, log_df):
        df = datahandler.get_frequent_requests(log_df)
        self.mysql.insert_frequent_requests(df)
        assert self.mysql.session.query(
            FrequentRequests).count() == df.shape[0]

    def test_client_errors_requests(self, log_df):
        df = datahandler.get_client_errors_requests(log_df)
        self.mysql.insert_client_errors_requests(df)
        assert self.mysql.session.query(ClientErrosRequests).count() == df.shape[0]

    def test_frequent_users(self, log_df):
        df = datahandler.get_frequent_users(log_df)
        self.mysql.insert_frequent_users(df)
        assert self.mysql.session.query(FrequentUsers).count() == df.shape[0]
