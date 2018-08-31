import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )

from ..models import Portfolio, Stock, Account, AccountRole


def usage(argv):
    """this is for usage when the server is running. Once server is running,
    type in the config uri and value in the terminal. In this case,
    pserve .development.ini.
    """
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    """this is the main method which takes in the system argument.
    This will parse the variables and config uri. And create a session.
    Based on the user, it will also assign a role, which is admin.
    """
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    # Create a connection(engine) to the DB
    engine = get_engine(settings)

    # Creates tables for our models in the DB
    Base.metadata.create_all(engine)

    # Below used for seeding DB

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        roles = ['admin', 'view']
        for role in roles:
            model = AccountRole(name=role)
            dbsession.add(model)
