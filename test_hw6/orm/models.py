from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CountRequests(Base):
    __tablename__ = 'count_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    total = Column(Integer, nullable=False)
