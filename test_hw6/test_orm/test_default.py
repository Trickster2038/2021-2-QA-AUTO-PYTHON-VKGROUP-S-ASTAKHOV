from sqlalchemy import func

from orm.models import CountRequests
from test_orm.base import MysqlBase


class TestMysqlCreate(MysqlBase):

    def test_requests_count(self, log_table, mysql_orm_client):
        counter = CountRequests(total=log_table.shape[0])
        mysql_orm_client.session.add(counter)
        mysql_orm_client.session.commit()
        assert mysql_orm_client.session.query(CountRequests).count() == 1
        
