from sqlalchemy.orm import relationship
from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey
)


from .meta import Base


class Portfolio(Base):
    """This is for the portfolio table in the database. Which will give the id,
    name, date created and updated. The account id and accounts are also shown
    and assigned foreign keys. This is to separate portfolio from the stock 
    table.
    """
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    accounts = relationship('Account', back_populates='portfolio')

    @classmethod
    def new(cls, request, **kwargs):
        """this is upon creation of a new entry in the database based on the keyword,
        portfolio. If no request, throw exception. If found via keyword, add 
        to the portfolio table.
        """
        if request.dbsession is None:
            raise DBAPIError

        # stocks = StocksLocation({'name': 'some name', 'zip_code': 98055})
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.portfolio == kwargs['portfolio']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """This will find the specific portfolio desired. If no request, then
        throw error.
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)
