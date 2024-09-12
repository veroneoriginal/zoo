from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from mainapp.models import Category
from api.serializers import CategoryModelSerializer


class CategoryViewSet(viewsets.ViewSet):

    @action(detail=True, methods=['get'])
    # pylint: disable=W0613 unused-argument
    def category_text_only(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        return Response({'category.title_name': category.title_name})

    # pylint: disable=W0613 unused-argument
    def list(self, request):
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)

    # pylint: disable=W0613 unused-argument
    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategoryModelSerializer(category)
        return Response(serializer.data)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CategoryCustomViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet,
    ):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
