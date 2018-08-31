from .associations import roles_association
from sqlalchemy.orm import relationship
from .meta import Base
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)


class AccountRole(Base):
    """this is for the account role table. This is to assign role(s) to a
    particular account. This will populate the table with the id, name,
    and accounts.
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    accounts = relationship('Account', secondary=roles_association, back_populates='roles')
