from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)


from .meta import Base


class StocksPortfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        # stocks = StocksLocation({'name': 'some name', 'zip_code': 98055})
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.portfolio == kwargs['portfolio']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)
