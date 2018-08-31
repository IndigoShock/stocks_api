from .portfolio import Portfolio
from .associations import roles_association
from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from cryptacular import bcrypt
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


manager = bcrypt.BCRYPTPasswordManager()


class Account(Base):
    """This is for the Accounts table in the database, which will
    give the id, email and password, portfolio and roles. The date
    created and updated will also show upon creation of an account.
    """
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    portfolio = relationship(Portfolio, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email=None, password=None):
        """Requires email and password, which will encode up to 10
        """
        self.email = email
        self.password = manager.encode(password, 10)  # unsafe

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user
        """
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        #  UNSAFE
        admin_role = request.dbsession.query(AccountRole).filter(
            AccountRole.name == 'admin').one_or_none()

        user.roles.append(admin_role)
        request.dbsession.flush()

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def one(cls, request, email=None):
        """This will show one account based on the email
        """
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """This will check the credentials of a specific account based on their email,
        and password. If it doesn't find it, then error thrown. Otherwise, it will check
        and say whether both are correct or not.
        """
        if request.dbsession is None:
            raise DBAPIError

        try:
            account = request.dbsession.query(cls).filter(
                cls.email == email).one_or_none()
        except DBAPIError:
            return None

        if account is not None:
            # check to see if passwords match:
            if manager.check(account.password, password):
                return account

        return None
