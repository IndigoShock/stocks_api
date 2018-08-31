from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIViewset(APIViewSet):
    def retrieve(self, request, id=None):
        """this will retrieve the company's API view. And populate into the
        database. At the moment, this will show whether the user correctly
        typed in the 4 letter symbol and retrieved information.
        """
        # http :6543/api/v1/company/{id}/

        # Use the 'id' to lookup that resource in the dB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200
        )

    # # Example
    # def list(self, request):
    #     # http :6543/api/v1/company/
    #     pass
