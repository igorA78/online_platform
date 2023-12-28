from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


from net.models import Net, Contact, Product, Provider
from net.permissions import UpdateDebtPermission
from net.serializers import NetSerializer, ViewNetSerializer, ContactSerializer, ProductSerializer, \
    ProviderSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Контактов
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Продуктов
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Поставшика
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class NetViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Сети
    """
    queryset = Net.objects.all()
    permission_classes = [IsAuthenticated, UpdateDebtPermission]
    filter_backends = [SearchFilter]
    search_fields = ['contact__country']

    def get_serializer_class(self):
        """
        В методе в зависимости от запроса идет выбор сериализатора
        """
        if self.action in ['list', 'retrieve']:
            return ViewNetSerializer
        return NetSerializer
