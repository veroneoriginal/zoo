from django.urls import (
    path,
    include,
)
from rest_framework.routers import (
    # SimpleRouter,
    DefaultRouter,
)
from api.views import CategoryViewSet
from api import api_views, generic_views, view_sets, filter_views, pagination_views

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('base', view_sets.CategoryViewSet, basename='base')
router.register('model', view_sets.CategoryModelViewSet, basename='model')
router.register('custom', view_sets.CategoryCustomViewSet, basename='custom')

# filter
router.register('queryset', filter_views.CategoryQuerysetFilterViewSet, basename='queryset')
router.register('param', filter_views.CategoryParamFilterViewSet, basename='param')
router.register('django', filter_views.CategoryDjangoFilterViewSet, basename='django')
router.register('custom-django', filter_views.CategoryCustomDjangoFilterViewSet,
                basename='custom-django')

# pagination
router.register('pagenumber', pagination_views.CategoryPageNumberPaginationViewSet,
                basename='pagenumber')
router.register('limitoffset', pagination_views.CategoryLimitOffsetPaginationviewSet,
                basename='limitoffset')


app_name = 'api'

urlpatterns = [
    # API views
    path('views/api-view/', api_views.CategoryAPIView.as_view()),
    path('views/func-api-view/', api_views.category_view),

    # generic views
    path('generic/create/', generic_views.CategoryCreateAPIView.as_view()),
    path('generic/list/', generic_views.CategoryListAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', generic_views.CategoryRetrieveAPIView.as_view()),
    path('generic/destroy/<int:pk>/', generic_views.CategoryDestroyAPIView.as_view()),
    path('generic/update/<int:pk>/', generic_views.CategoryUpdateAPIView.as_view()),

    # подключаем интерфейс
    path('viewsets/', include(router.urls)),

    # filter
    path('filters/kwargs/<str:name>/', filter_views.CategoryKwargsFilterView.as_view()),

]
