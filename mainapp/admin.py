# В этом модуле код, который настроен для работы с Django Admin.
# Django Admin — это встроенная панель администратора,
# которая позволяет управлять моделями данных через веб-интерфейс.

# admin - модуль, который предоставляет функциональность административной панели.
from django.contrib import admin
from .models import Animal, Category, Food, WildAnimal, HomeAnimal

# регистрация модели Category в административной панели
admin.site.register(Category)


# ______________________________________________________________
class FoodAdmin(admin.ModelAdmin):
    """Класс настройки админки для еды"""

    # list_display определяет, какие поля модели будут отображаться в админке
    list_display = ('id', 'name')

    @admin.action(description="Download Food")
    def download_food(self, queryset):
        with open('food.txt', 'w', encoding='utf-8') as f:
            for food in queryset.all():
                f.write(f'{food.name}\n')

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
