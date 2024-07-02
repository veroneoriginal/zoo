from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Animal


# данные запроса
def index_view(request):
    return render(request, 'mainapp/index.html')


# def category_list_view(request):
#     category_list = Category.objects.all()
#     context = {'category_list': category_list}
#     return render(request, 'mainapp/category_list.html', context=context)


class CategoryListView(ListView):
    model = Category
    # ordering определяет как происходит сортировка
    ordering = ['pk']  # ordering = ['name']

    # пагинация - сколько объектов выводить на страницу
    # paginate_by = 5

    # передать свойства внутрь класса
    # template_name =

    # названия переменной в шаблоне
    # context_object_name =

    # get - гет запрос

    # get_queriset - получение данных

    # если мы хотим добавить что-то в контекст / передача контекста в шаблон
    # get_context_data
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['some_text'] = "some text"
        return context


class CategoryDetailView(DetailView):
    model = Category

    # get - гет запрос
    # get_context_data - передача контекста в шаблон
    # get_queriset - получение данных
    # get_object - получение одного объекта


class CategoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy('mainapp:category_list')

    # get - гет запрос
    # get_context_data - передача контекста в шаблон
    # post
    # form_valid
    # get_success_url


class CategoryUpdateView(UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy('mainapp:category_list')

    # get - гет запрос
    # get_context_data - передача контекста в шаблон
    # post
    # form_valid
    # get_object - получение одного объекта
    # get_success_url


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('mainapp:category_list')

    # get - гет запрос
    # get_context_data - передача контекста в шаблон
    # post
    # form_valid
    # get_object
    # get_success_url


class AnimalListView(ListView):
    model = Animal
    template_name = 'mainapp/animals.html'

    def get(self, request, *args, **kwargs):
        self.category_id = request.GET.get('category_id', None)
        print("CATEGORY_ID", self.category_id)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.category_id is not None:
            queryset = queryset.filter(category_id=self.category_id)
        return queryset
