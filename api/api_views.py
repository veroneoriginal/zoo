from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CategoryModelSerializer
from mainapp.models import Category


class CategoryAPIView(APIView):
    renderer_classes = [JSONRenderer]

    # pylint: disable=W0622 redefined-builtin
    # pylint: disable=W0613 unused-argument
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)


# тоже самое только функцией
@api_view(['GET'])
@renderer_classes([JSONRenderer])
# pylint: disable=W0613 unused-argument
def category_view(request):
    categories = Category.objects.all()
    serializer = CategoryModelSerializer(categories, many=True)
    return Response(serializer.data)
