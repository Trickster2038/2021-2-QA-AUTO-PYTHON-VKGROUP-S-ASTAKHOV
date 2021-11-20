from sqlalchemy import func

from orm.models import CountRequests, TypedRequests, ClientErrosRequests
from test_orm.base import MysqlBase
import pandas as pd


class TestMysqlCreate(MysqlBase):

    def test_requests_count(self, log_df, mysql_orm_client):
        counter = CountRequests(total=log_df.shape[0])
        mysql_orm_client.session.add(counter)
        mysql_orm_client.session.commit()
        assert mysql_orm_client.session.query(CountRequests).count() == 1

    def test_requests_by_type(self, log_df, mysql_orm_client):
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
            mysql_orm_client.session.add(request_cnt)
            mysql_orm_client.session.commit()
        assert mysql_orm_client.session.query(TypedRequests).count() == 4

    def test_client_errors_requests(self, log_df, mysql_orm_client):
        df_filtered = log_df.query(
            "status >= 400 and status < 500 and size != '-'").iloc[:, 0:4].copy()
        df_filtered["size"] = df_filtered["size"].astype(int)
        df = df_filtered.sort_values(
            "size", ascending=False).head(5).reset_index(drop=True)

        for index, row in df.iterrows():
            request_cnt = ClientErrosRequests(ip=row['ip'], url=row['url'],
                                              status=row['status'], size=row['size'])
            mysql_orm_client.session.add(request_cnt)
            mysql_orm_client.session.commit()
        assert mysql_orm_client.session.query(ClientErrosRequests).count() == 5
