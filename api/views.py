from rest_framework.viewsets import ModelViewSet
from api.serializers import (CategoryModelSerializer,
                             CategoryModelSerializerOther)
from api.permissions import OnlyForOneUser
from mainapp.models import Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializerOther
    # serializer_class = CategoryModelSerializer
    permission_classes = [OnlyForOneUser]

    def get_queryset(self):
        print('VERSION', self.request.version)
        return super().get_queryset()

    def get_serializer_class(self):
        version = self.request.version
        if version == 'v1.0':
            return CategoryModelSerializer
        else:
            return CategoryModelSerializerOther
