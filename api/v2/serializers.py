from rest_framework.serializers import (
    ModelSerializer,
)
from mainapp.models import Category


class CategoryModelSerializerOther(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('updated_at', 'created_at')
