from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from mainapp.models import Category
from api.serializers import CategoryModelSerializer

class CategoryPageNumberPaginationViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class CategoryLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class CategoryLimitOffsetPaginationviewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    pagination_class = CategoryLimitOffsetPagination
