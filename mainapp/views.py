from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.db.models import Case, When, Value, IntegerField
from mainapp.models import Category, Animal
from mainapp.forms import AnimalForm, ContactForm


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


class CategoryCreateView(LoginRequiredMixin, CreateView):
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

    def get_queryset(self):
        # Все животные
        queryset = Animal.objects.select_related('wildanimal').annotate(
            age=Case(
                When(wildanimal__isnull=False, then='wildanimal__age'),
                default=Value(None),
                output_field=IntegerField()
            )
        )

        queryset = queryset.select_related('category')
        queryset = queryset.prefetch_related('food')

        return queryset


class AnimalCreateView(CreateView):
    """Представление для создания животных"""

    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('mainapp:animal_list')


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('mainapp:index')
    template_name = 'mainapp/contact.html'

    # Переопределяем метод
    def form_valid(self, form):
        data = form.cleaned_data
        print('MESSAGE', data['message'])
        return super().form_valid(form)
