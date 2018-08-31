from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models import Account
import json


class AuthAPIViewset(APIViewSet):
    def create(self, request, auth=None):
        """this will create the view for the authorization. Once they register, the
        email and password will be checked. If it does not pass, user will have
        a bad request. If they do, then they will have a token for the roles
        based on their email. If they login and are authenticated through
        their email and password, they will be assigned their role again.
        Otherwise, they will receive an error of Not Authorized.
        And beyond not functioning, it will show a Not Found Error.
        """
        data = json.loads(request.body)

        if auth == 'register':
            try:
                user = Account.new(
                    request,
                    data['email'],
                    data['password'])
            except (IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)

            # TODO: Refactor this to use JSON Web Token
            return Response(
                json_body={
                    'token': request.create_jwt_token(
                        user.email,
                        roles=[role.name for role in user.roles],
                        userName=user.email,
                    )
                },
                status=201
            )

        if auth == 'login':
            authenticated = Account.check_credentials(request, data['email'], data['password'])

            if authenticated:
                return Response(
                    json_body={
                         'token': request.create_jwt_token(
                            authenticated.email,
                            roles=[role.name for role in authenticated.roles],
                            userName=authenticated.email,
                         )
                    }
                )
            return Response(json='Not Authorized', status=401)

        return Response(json='Not Found', status=404)
