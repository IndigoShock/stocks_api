from .weather_location import WeatherLocation
from .associations import roles_association
from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from .role import AccountRole
from datetime import datetime as dt
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    DateTime,
)


from .meta import Base


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    locations = relationship(WeatherLocation, back_populates='account')
    roles = relationship(AccountRole, secondary=roles_association, back_populate='account')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password  # unsafe

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user
        """
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)
