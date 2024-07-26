from django.db.models import Value, CharField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Category, Animal, WildAnimal
from .forms import AnimalForm, ContactForm


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

    def get_context_data(self, *args, **kwargs):
        # context = super().get_context_data(*args, **kwargs)
        # context['category_list'] = Category.objects.all()
        # return context
        context = super().get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.all()

        # Получение всех животных
        all_animals = Animal.objects.all()
        wild_animals = WildAnimal.objects.all()

        wild_animal_ids = wild_animals.values_list('id', flat=True)
        domestic_animals = all_animals.exclude(id__in=wild_animal_ids)

        combined_list = list(domestic_animals) + list(wild_animals)

        if self.category_id is not None:
            combined_list = [animal for animal in combined_list if animal.category_id == int(self.category_id)]

        context['object_list'] = combined_list
        context['object_count'] = len(combined_list)

        return context

    def get(self, request, *args, **kwargs):
        self.category_id = request.GET.get('category_id', None)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        object_count = Animal.objects.all()
        return len(object_count)
        # # Все животные
        # all_animals = super().get_queryset().annotate(animal_type=Value('Animal', output_field=CharField()))
        #
        # # Дикие животные
        # wild_animals = WildAnimal.objects.annotate(animal_type=Value('WildAnimal', output_field=CharField()))
        #
        # # Объединение домашних и диких животных
        # queryset = all_animals.union(wild_animals)
        #
        # # Применение фильтра по категории, если указан
        # if self.category_id is not None:
        #     queryset = [animal for animal in queryset if animal.category_id == int(self.category_id)]

        # return queryset

    # def get_queryset(self):
    #     # все животные
    #     all_animals = super().get_queryset()
    #
    #     # дикие животные с указанием возраста
    #     wild_animals = WildAnimal.objects.all()
    #
    #     # домашние животные = все животные - дикие животные
    #     wild_animal_ids = wild_animals.values_list('id', flat=True)
    #     home_animals = all_animals.exclude(id__in=wild_animal_ids)
    #
    #     # Объединение домашних и диких животных
    #     queryset = list(home_animals) + list(wild_animals)
    #
    #     return queryset

    #     # if self.category_id is not None:
    #     #     queryset = queryset.filter(category_id=self.category_id)
    #
    #     queryset = queryset.select_related('category')
    #     queryset = queryset.prefetch_related('food')
    #
    #     # for wild_animal in queryset:
    #     #     print(f"Wild_animal: {wild_animal.name}, Age: {wild_animal.age}")
    #
    #     # for animal in queryset:
    #     #     print(animal.show_food)


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
