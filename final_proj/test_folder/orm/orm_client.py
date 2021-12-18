import sqlalchemy
from sqlalchemy.orm import sessionmaker
import allure

from orm.models import Base, User

class MysqlORMClient:

    def __init__(self, user, password, db_name, host='0.0.0.0', port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        # db = self.db_name if db_created else ''
        db = self.db_name
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        sm = sessionmaker(bind=self.connection.engine)  # session creation wrapper
        self.session = sm()

    def truncate_table(self):
        self.connect()
        self.session.query(User).delete()
        self.session.commit()
        self.connection.close()

    def execute_query(self, query, fetch=True):
            res = self.connection.execute(query)
            if fetch:
                return res.fetchall()

    @allure.step("DB: Count") 
    def count(self, class_name):
        self.session.commit()
        cnt = self.session.query(class_name).count()
        allure.attach(str(cnt), 'Count', allure.attachment_type.TEXT)
        return cnt

    @allure.step("DB: Access check")
    def get_access(self, person):
        self.session.commit()
        access = self.session.query(User.access).filter(User.username == person.username).one()[0]
        allure.attach(str(access), 'Access', allure.attachment_type.TEXT)
        return access