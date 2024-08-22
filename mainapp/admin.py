# В этом модуле код, который настроен для работы с Django Admin.
# Django Admin — это встроенная панель администратора,
# которая позволяет управлять моделями данных через веб-интерфейс.

# import time
# admin - модуль, который предоставляет функциональность административной панели.
from django.contrib import admin
import django_rq
from .models import Animal, Category, Food, WildAnimal, HomeAnimal
from .tasks import save_report

# регистрация модели Category в административной панели
admin.site.register(Category)


# pylint: disable=W0613 unused-argument
class FoodAdmin(admin.ModelAdmin):
    """Класс настройки админки для еды"""

    list_display = ('id', 'name')

    @admin.action(description="Download Food")
    def download_food(self, request, queryset):
        django_rq.enqueue(save_report, queryset=queryset)

    # зарегать для отображениия в админке
    actions = [download_food]


# регистрация модели Food в административной панели
admin.site.register(Food, FoodAdmin)


# ______________________________________________________________
class AnimalAdmin(admin.ModelAdmin):
    """Класс настройки админки для отображения животных"""

    list_display = ('name', 'category', 'show_food')


# регистрация модели животных и диких животных в административной панели
admin.site.register(Animal, AnimalAdmin)
admin.site.register(WildAnimal, AnimalAdmin)


class HomeAnimalAdmin(admin.ModelAdmin):
    """Класс настройки админки для отображения домашних животных"""
    list_display = ('name', 'category', 'last_owner_name')


# регистрация модели домашних животных в административной панели
admin.site.register(HomeAnimal, HomeAnimalAdmin)
