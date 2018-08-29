from pyramid_restful.routers import ViewSetRouter
from .views.portfolio import StockAPIViewset
from .views.company import CompanyAPIViewset
from .views.auth import AuthAPIViewset
# from .views import CompanyAPIViewSet


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/stocks', StockAPIViewset, 'stocks')
    router.register('api/v1/auth/{auth}', AuthAPIViewset, 'auth')
