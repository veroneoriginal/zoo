from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Animal(models.Model):
    name = models.CharField(max_length=100)
    # 1 - 1, 1 - *, * - *
    # 1 категория - много животных
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return f'{self.name}'
