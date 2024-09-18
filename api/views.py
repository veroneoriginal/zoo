from rest_framework.viewsets import ModelViewSet
from api.serializers import CategoryModelSerializer
from api.permissions import OnlyForOneUser
from mainapp.models import Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [OnlyForOneUser]
