from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import filters
from rest_framework import status
from all_product.models import Category, Product, Location
from .serializers import ProductSerializer, CategorySerializer, LocationsSerializer, AllProductSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.all_product import permissions, serializers


class MyProductViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.Update, IsAuthenticated,)
    model = Product
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'id', 'category__name',)

    # permission_classes = (permissions.Update,IsAuthenticated,)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(owner=self.request.user)

    def get_queryset(self):
        qs = Product.objects.all()
        qs = qs.filter(owner=self.request.user)
        return qs


class MyCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.Update, IsAuthenticated,)
    model = Category
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'id', 'category__name',)
    def get_queryset(self):

        qs = Category.objects.all()
    # qs = qs.filter(owner=self.request.user)
        return qs


class AllProductViewSet(viewsets.ReadOnlyModelViewSet):
    model = Product
    serializer_class = AllProductSerializer
    # permission_classes = (permissions.Update, IsAuthenticated)
    def get_queryset(self):
        qs = Product.objects.all()
        # qs = qs.filter(owner=self.request.user)
        return qs


class MyLocationsViewSet(viewsets.ModelViewSet):
    model = Location
    serializer_class = LocationsSerializer

    permission_classes = (permissions.Update, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'id', 'category__name',)

    def get_queryset(self):
        qs = Location.objects.all()
        # qs = qs.filter(owner=self.request.user)
        return qs


# # class MyCartViewSet(viewsets.ModelViewSet):
# #     model = Cart
# #     serializer_class = CartSerializer
# #
# #     def get_queryset(self):
# #         qs = Cart.objects.all()
# #         # qs = qs.filter(owner=self.request.user)
# #         return qs


@csrf_exempt
def product_list(request, owner):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def category_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        category = Category.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)


@csrf_exempt
def location_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        location = Location.objects.all()
        serializer = LocationsSerializer(location, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def locations_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        location = Location.get(pk=pk)

    except Location.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocationsSerializer(location)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LocationsSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)

# @csrf_exempt
# def all_product_list(request, owner):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#
#         alproducts = AllProduct.objects.all()
#         serializer = AllProductSerializer(alproducts, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
