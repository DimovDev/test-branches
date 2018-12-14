from rest_framework import serializers
from all_product.models import Product, Category, Location


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'owner', 'id', 'category', 'location', 'phone_number', 'name', 'image', 'description', 'price', 'stock',
            'available',
            'created',
            'updated',)
        read_only_fields = ['owner']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'slug',)


class AllProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
        'id', 'owner', 'location', 'phone_number', 'category', 'name', 'image', 'description', 'price', 'stock',
        'available',
        'created', 'updated')
        list_editable = ['price', 'stock', 'available']
        read_only_fields = [ 'owner',]
