import datetime

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String)

from baseCore.base import Base, Engine


class Filter(Base):
    __tablename__ = "Filter"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False, unique=True)


class ExecutorService(Base):
    __tablename__ = "ExecutorService"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    category = Column(Integer, ForeignKey(Filter.id), nullable=False)
    name = Column(String, nullable=False, unique=True)
    rating = Column(Float, nullable=False)
    description = Column(String, nullable=False, unique=True)
    longitude = Column(Integer, nullable=False)
    latitude = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False, unique=True)
    address = Column(String, nullable=False)
    creation_date = Column(DateTime,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    status = Column(Boolean, default=True, nullable=False)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False, default="Имя")
    surname = Column(String, nullable=False, default="Фамилия")
    favorites = Column(String, default=None)
    phone = Column(Integer, unique=True, nullable=False)
    address = Column(String, default=None)   #nullable=False
    creation_date = Column(DateTime,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    status = Column(Boolean, default=True, nullable=False)


class UserFeedback(Base):
    __tablename__ = "UserFeedback"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    userid = Column(Integer, ForeignKey(User.id), nullable=False)
    serviceid = Column(Integer, ForeignKey(ExecutorService.id), nullable=False)
    mark = Column(Integer, nullable=False)
    feed = Column(String, nullable=False, unique=True)
    creation_date = Column(DateTime,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    status = Column(Boolean, default=True, nullable=False)


class ExecOne(Base):
    __tablename__ = "ExecOne"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    parrentserviceid = Column(Integer,
                              ForeignKey(ExecutorService.id),
                              nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    creation_date = Column(DateTime,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    status = Column(Boolean, default=True, nullable=False)


class UserOrder(Base):
    __tablename__ = "UserOrder"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    userid = Column(Integer, ForeignKey(User.id), nullable=False)
    serviceid = Column(Integer, ForeignKey(ExecutorService.id), nullable=False)
    uslugaid = Column(Integer, ForeignKey(ExecOne.id), nullable=False)
    ordertime = Column(DateTime,
                       default=datetime.datetime.utcnow,
                       nullable=False)
    runtime = Column(DateTime, nullable=False)
    isCompleted = Column(Boolean, default=False, nullable=False)
    accepted = Column(Boolean, default=False, nullable=False)


class UserVerificationSession(Base):
    __tablename__ = "UserVerificationSession"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    phone = Column(Integer, nullable=False, unique=True)
    code = Column(Integer, nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(Engine)
