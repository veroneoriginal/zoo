from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampMixin):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def title_name(self):
        return self.name.upper()


class Food(TimeStampMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Animal(TimeStampMixin):
    name = models.CharField(max_length=100)
    # 1 - 1, 1 - *, * - *
    # 1 категория - много животных
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return f'{self.name}'

    @property
    def show_food(self):
        food = []
        food_queryset = self.food.all()
        for food_obj in food_queryset:
            food.append(food_obj.name)
        food_str = ', '.join(food)
        return food_str

    def get_category_name(self):
        return self.category.name


class WildAnimal(Animal):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)


class HomeAnimal(Animal):
    last_owner_name = models.CharField(max_length=100, blank=True, null=True)


class AnimalCard(TimeStampMixin):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
