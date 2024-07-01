from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
    # ordering определяет как происходит сортировка
    ordering = ['pk']
    # ordering = ['name']

    # пагинация - сколько объектов выводить на страницу
    # paginate_by = 5


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy('mainapp:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy('mainapp:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('mainapp:category_list')
