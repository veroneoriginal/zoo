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
