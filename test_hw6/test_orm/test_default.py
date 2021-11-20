from sqlalchemy import func
from sqlalchemy.sql.functions import count

from orm.models import CountRequests, FrequentRequests, FrequentUsers, TypedRequests, ClientErrosRequests
from test_orm.base import MysqlBase
import pandas as pd
import pytest

@pytest.mark.ORM
class TestMysqlLogSaving(MysqlBase):

    def test_requests_count(self, log_df):
        counter = CountRequests(total=log_df.shape[0])
        self.mysql.session.add(counter)
        self.mysql.session.commit()
        assert self.mysql.session.query(CountRequests).count() == 1

    def test_requests_by_type(self, log_df):
        df_methods_1 = log_df.copy()

        # generating methods column
        df_methods_1["method"] = df_methods_1.apply(
            lambda row: row["url"].split()[0], axis=1)
        df_methods_2 = pd.DataFrame(df_methods_1["method"])

        # grouping by method
        df_methods_2["cnt"] = 0
        df_meths = df_methods_2.groupby(
            by=["method"], as_index=False).count().reset_index(drop=True)

        # removing trash
        df = df_meths.loc[(df_meths["method"].astype(
            'str').str.len() < 10)].reset_index(drop=True)

        for index, row in df.iterrows():
            request_cnt = TypedRequests(method=row['method'], count=row['cnt'])
            self.mysql.session.add(request_cnt)
            self.mysql.session.commit()
        assert self.mysql.session.query(TypedRequests).count() == 4

    def test_frequent_requests(self, log_df):
        df_urls = pd.DataFrame(log_df.iloc[:, 1])
        df_urls["cnt"] = 0
        df_urls2 = df_urls.copy()
        df_urls2["url_without_params"] = df_urls.apply(
            lambda row: row["url"].split()[1], axis=1)
        del df_urls2["url"]
        df_urls_g = df_urls2.groupby(
            by=["url_without_params"], as_index=False).count()
        df = df_urls_g.sort_values("cnt", ascending=False).head(
            10).reset_index(drop=True)

        for index, row in df.iterrows():
            request_cnt = FrequentRequests(
                url=row['url_without_params'], count=row['cnt'])
            self.mysql.session.add(request_cnt)
            self.mysql.session.commit()
        assert self.mysql.session.query(FrequentRequests).count() == 10

    def test_client_errors_requests(self, log_df):
        df_filtered = log_df.query(
            "status >= 400 and status < 500 and size != '-'").iloc[:, 0:4].copy()
        df_filtered["size"] = df_filtered["size"].astype(int)
        df = df_filtered.sort_values(
            "size", ascending=False).head(5).reset_index(drop=True)

        for index, row in df.iterrows():
            request_cnt = ClientErrosRequests(ip=row['ip'], url=row['url'],
                                              status=row['status'], size=row['size'])
            self.mysql.session.add(request_cnt)
            self.mysql.session.commit()
        assert self.mysql.session.query(ClientErrosRequests).count() == 5

    def test_frequent_users(self, log_df):
        df_5xx = log_df.query("status >= 500 and status < 600").iloc[:, [0]]
        df_5xx["cnt"] = 0
        df = df_5xx.groupby(by=["ip"], as_index=False).count().sort_values("cnt", ascending=False).head(5).reset_index(drop=True)

        for index, row in df.iterrows():
            request_cnt = FrequentUsers(ip=row['ip'], count=row['cnt'])
            self.mysql.session.add(request_cnt)
            self.mysql.session.commit()
        assert self.mysql.session.query(FrequentUsers).count() == 5
