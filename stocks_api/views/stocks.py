from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import IntegrityError, DataError
from ..models.schemas import StocksPortfolioSchema
from ..models import StocksPortfolio
import requests
import json


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """
    """
    url = 'https://api.iextrading.com/1.0'.format(
        requests.matchdict['zip_code'],
        '(API_KEY)',
    )
    response = request.get(url)

    return Response(json=response.json(), status=200)


class StockAPIViewset(APIViewSet):
    """
    """
    def create(self, request):
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'stocks' not in kwargs:
            return Response(json='Expected value; stocks', status=400)

        try:
            stocks = StocksPortfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(
                json='Duplicate Key Error. Stock already exists', status=409)

        schema = StocksPortfolioSchema()
        data = schema.dump(stocks).data

        return Response(json=data, status=201)

        # return Response(
        #     json={'message': 'Created a new resource'},
        #     status=201)

    def list(self, request):
        return Response(
            json={'message': 'Provided a list of stocks'},
            status=200)

    def retrieve(self, request, id=None):
        # http :6543/api/v1/company/{id}/

        # Use the 'id' to lookup that resource in the dB,
        # Formulate a response and send it back to the client
        return Response(
            json={'message': 'Provided a single resource'},
            status=200)

    def destroy(self, request, id=None):
        """
        """
        if not id:
            return Response(json='Not Found', status=404)

        try:
            StocksPortfolio.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)
