from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from mainapp.models import Category
from api.serializers import CategoryModelSerializer


class CategoryQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.filter(name__contains='едве')


class CategoryKwargsFilterView(ListAPIView):
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Category.objects.filter(name__contains=name)


class CategoryParamFilterViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        categorys = Category.objects.all()
        if name:
            categorys = categorys.filter(name__contains=name)
        return categorys


# когда хотим настроить точное совпадение полей
class CategoryDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filterset_fields = ['name']


# когда хотим настроить какое-то сложное совпадение
class CategoryCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
