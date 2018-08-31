from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """this is the default view, if there was a front end. At the moment,
    this is for the terminal.
    """
    message = '''
        GET / - Base API route\n
        POST /api/v1/auth/ - Register a new account\n
        GET /api/v1/auth/ - Login to an existing account\n
        GET /api/v1/weather/ - Retrieve all weather information\n
        GET /api/v1/weather/<int>/ - Retrieve specific weather record\n
        POST /api/v1/weather/ - Create new weather record\n
        DELETE /api/v1/weather/<int>/ - Remove existing weather record\n
    '''
    return Response(body=message, content_type='text/plain', status=200)
