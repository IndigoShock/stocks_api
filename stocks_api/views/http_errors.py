from pyramid.response import Response
from pyramid.view import forbidden_view_config, notfound_view_config


@forbidden_view_config()
def forbidden(request):
    """if a user is not approved, they will be shown this error message of 403
    """
    return Response(json='Forbidden', status=403)


@notfound_view_config()
def not_found(request):
    """if a user could not find whatever they were typing in, they will see
    a 404 error status page
    """
    return Response(json='Not Found', status=404)
