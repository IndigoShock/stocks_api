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
    """This will populate the stock table in the database. It will give the
    id, symbol, companyName, exchange, industry, website,
    description, CEO, issueType, sector, date_created, date_updated.
    """
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    company_name = Column(Text)
    exchange = Column(Integer)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    ceo = Column(Text)
    issue_type = Column(Text)
    sector = Column(Text)

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        """this is upon creation of a new entry in the database based on the keyword,
        symbol. If no request, throw exception. If found via keyword, add
        to the stock table.
        """
        if request.dbsession is None:
            raise DBAPIError

        # stocks = StocksLocation({'name': 'some name', 'zip_code': 98055})
        stocks = cls(**kwargs)
        request.dbsession.add(stocks)

        return request.dbsession.query(cls).filter(
            cls.stock == kwargs['symbol']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """This will find the specific stock desired. If no request, then
        throw error.
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def destroy(cls, request=None, pk=None):
        """This will destroy the record. If no request, return error. But if so,
        then filter all other results to the specific one and delete it based 
        on the primary key.
        """
        if request.dbsession is None:
            raise DBAPIError

        # return request.dbsession.query(cls).get(pk).delete()
        return request.dbsession.query(cls).filter(
            cls.accounts.email == request.authenticated_userid).filter(
                cls.id == pk).delete()
