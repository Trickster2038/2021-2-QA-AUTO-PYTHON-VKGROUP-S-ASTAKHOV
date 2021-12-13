from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CountRequests(Base):
    __tablename__ = 'count_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    total = Column(Integer, nullable=False)


class TypedRequests(Base):
    __tablename__ = 'typed_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(length=10), nullable=False)
    count = Column(Integer, nullable=False)


class FrequentRequests(Base):
    __tablename__ = 'frequent_requests'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(length=400), nullable=False)
    count = Column(Integer, nullable=False)


class ClientErrosRequests(Base):
    __tablename__ = 'client_errors_requests'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(length=36), nullable=False)
    url = Column(String(length=400), nullable=False)
    status = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)


class FrequentUsers(Base):
    __tablename__ = 'frequent_users'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(length=36), nullable=False)
    count = Column(Integer, nullable=False)
