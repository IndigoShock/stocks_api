from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


# class StockAPIView(APIViewSet):
#     def list(self, request):
#         return Response(json={'message': 'listing all the records'}, status=200)

#     def retrieve(self, request):
#         return Response(json={'message': 'listing one of the records'}, status=200)

#     def create(self, request):
#         return Response(json={'message': 'creating a new record'}, status=201)

#     def destroy(self, request):
#         return Response(json={'message': 'deleted the record'}, status=204)


class StockAPIViewset(APIViewSet):

    def retrieve(self, request, id=None):
        # http :6543/api/v1/company/{id}/

        # Use the 'id' to lookup that resource in the dB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200)

    def list(self, request):
        return Response(
            json={'message': 'Provided a list of stocks'},
            status=200)

    def create(self, request):
        return Response(
            json={'message': 'Created a new resource'},
            status=201)

    def destroy(self, request, id=None):
        return Response(
            status=204)
