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


class Stock(Base):
    """id, symbol, companyName, exchange, industry, website,
    description, CEO, issueType, sector, date_created, date_updated
    """
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    companyName = Column(Text)
    exchange = Column(Integer)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    CEO = Column(Text)
    issueType = Column(Text)
    sector = Column(Text)

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        # stocks = StocksLocation({'name': 'some name', 'zip_code': 98055})
        stocks = cls(**kwargs)
        request.dbsession.add(stocks)

        return request.dbsession.query(cls).filter(
            cls.stock == kwargs['stock']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def destroy(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        # return request.dbsession.query(cls).get(pk).delete()
        return request.dbsession.query(cls).filter(
            cls.id == pk).delete()
