from django.shortcuts import render
from django.views.generic import ListView
from .models import Category


# данные запроса
def index_view(request):
    return render(request, 'mainapp/index.html')


def category_list_view(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'mainapp/category_list.html', context=context)


class CategoryListView(ListView):
    model = Category
