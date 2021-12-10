import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from orm.models import Base, ClientErrosRequests, CountRequests, FrequentRequests, FrequentUsers, TypedRequests


class MysqlORMClient:

    def __init__(self, user, password, db_name, host='127.0.0.1', port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        sm = sessionmaker(bind=self.connection.engine)  # session creation wrapper
        self.session = sm()

    def recreate_db(self):
        self.connect(db_created=False)

        # these two requests we need to do in ras SQL syntax
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()

    def create_count_table(self):
        if not inspect(self.engine).has_table('count_requests'):
            Base.metadata.tables['count_requests'].create(self.engine)

    def create_typed_requests_table(self):
        if not inspect(self.engine).has_table('typed_requests'):
            Base.metadata.tables['typed_requests'].create(self.engine)

    def create_client_errors_requests_table(self):
        if not inspect(self.engine).has_table('client_errors_requests'):
            Base.metadata.tables['client_errors_requests'].create(self.engine)

    def create_frequent_requests_table(self):
        if not inspect(self.engine).has_table('frequent_requests'):
            Base.metadata.tables['frequent_requests'].create(self.engine)

    def create_frequent_users_table(self):
        if not inspect(self.engine).has_table('frequent_users'):
            Base.metadata.tables['frequent_users'].create(self.engine)


    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def insert_count_requests(self, df):
        counter = CountRequests(total=df.shape[0])
        self.session.add(counter)
        self.session.commit()

    def insert_typed_requests(self, df):
        for index, row in df.iterrows():
            request_cnt = TypedRequests(method=row['method'], count=row['cnt'])
            self.session.add(request_cnt)
            self.session.commit()

    def insert_frequent_requests(self, df):
        for index, row in df.iterrows():
            request_cnt = FrequentRequests(
                url=row['url_without_params'], count=row['cnt'])
            self.session.add(request_cnt)
            self.session.commit()

    def insert_client_errors_requests(self, df):
        for index, row in df.iterrows():
            request_cnt = ClientErrosRequests(ip=row['ip'], url=row['url'],
                                              status=row['status'], size=row['size'])
            self.session.add(request_cnt)
            self.session.commit()

    def insert_frequent_users(self, df):
        for index, row in df.iterrows():
            request_cnt = FrequentUsers(ip=row['ip'], count=row['cnt'])
            self.session.add(request_cnt)
            self.session.commit()