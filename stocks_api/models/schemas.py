from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio, Stock, Account, AccountRole


class AccountRoleSchema(ModelSchema):
    """this schema model is based on the account role. The meta class references
    the meta model and will be filled with the Role model.
    """
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    """this schema model is based on the account. The meta class references
    the meta model and will be filled with the Account model. the roles
    field will also use the role schema from above and use the name
    """
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


class PortfolioSchema(ModelSchema):
    """this schema model is based on the portfolio. this will build upon the
    two above schemas, the roles and accounts. the account section will not
    include the password, locations, roles and dates for security reasons.
    """
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'locations', 'roles', 'date_created', 'date_updated',
    ))

    class Meta:
        model = Portfolio


class StockSchema(ModelSchema):
    """this schema model is based on the stock. this will also build on
    the account and role schemas. similarly true as the portfolio schema,
    the account section will not include the password, locations, roles,
    and dates for security reasons
    """
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'locations', 'roles', 'date_created', 'date_updated',
    ))

    class Meta:
        model = Stock
