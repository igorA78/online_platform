from rest_framework import serializers
from .models import Net, Contact, Product, Provider


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_email', 'country', 'city', 'street', 'house_number']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model', 'release_date']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['name']


class ViewNetSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра сети
    """
    contact = ContactSerializer()
    product = ProductSerializer(many=True, read_only=True)
    provider = ProviderSerializer()

    class Meta:
        model = Net
        fields = ['name', 'category', 'contact', 'product', 'provider', 'debt', 'created_at']


class NetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Net
        fields = '__all__'

    def validate(self, data):
        """
        В данном методе сравнивается категория поставщика с категорией сети
        """
        provider_category = data['provider'].category
        net_category = data['category']
        if not net_category-1 == provider_category:
            raise serializers.ValidationError(
                'Категория поставщика должна быть предыдущей по иерархии '
            )
        return data
