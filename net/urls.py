from rest_framework import routers

from net.apps import NetConfig
from net.views import NetViewSet, ContactViewSet, ProductViewSet, ProviderViewSet

app_name = NetConfig.name

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('net', NetViewSet)
router.register('contact', ContactViewSet)
router.register('product', ProductViewSet)
router.register('supplier', ProviderViewSet)
urlpatterns += router.urls
