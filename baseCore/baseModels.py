import datetime

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String, Time)
from sqlalchemy.orm import relationship

from baseCore.base import Base, Engine


class Repr():
    def __repr__(self) -> str:
        return str(self.__dict__)


class Filter(Base, Repr):
    __tablename__ = "Filter"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False, unique=True)


class AssociationExecToExpert(Base, Repr):
    __tablename__ = "AssociationExecToExpert"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    expert_id = Column(Integer, ForeignKey('Expert.id'), nullable=False)
    expert_id = relationship('Expert')
    exec_id = Column(Integer, ForeignKey('ExecOne.id'), nullable=False)


class Expert(Base, Repr):
    __tablename__ = 'Expert'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    organisation_id = Column(Integer, nullable=False)
    creation_date = Column(DateTime,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    status = Column(Boolean, default=True, nullable=False)


class ExecutorService(Base, Repr):
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


class User(Base, Repr):
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


class UserFeedback(Base, Repr):
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


class ExecOne(Base, Repr):
    __tablename__ = "ExecOne"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    parrentserviceid = Column(Integer,
                              ForeignKey(ExecutorService.id),
                              nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    experts = relationship('AssociationExecToExpert')
    duration = Column(Time, nullable=False)
    creation_date = Column(DateTime,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    status = Column(Boolean, default=True, nullable=False)


class UserOrder(Base, Repr):
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


class UserVerificationSession(Base, Repr):
    __tablename__ = "UserVerificationSession"

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    phone = Column(Integer, nullable=False, unique=True)
    code = Column(Integer, nullable=False)

if __name__ == "__main__":
    Base.metadata.create_all(Engine)
