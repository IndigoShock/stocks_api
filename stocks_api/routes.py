from pyramid_restful.routers import ViewSetRouter
from .views import StocksAPIView, CompanyAPIViewSet
from .views.auth import AuthAPIViewSet
# from .views import CompanyAPIViewSet


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/company', CompanyAPIViewSet, 'company')
    router.register('api/v1/stocks', StocksAPIView, 'stocks')
    router.register('api/v1/auth/{auth}', AuthAPIViewSet, 'auth')
