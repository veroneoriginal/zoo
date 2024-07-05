from django import forms
from .models import Animal, Category, Food


class AnimalForm(forms.ModelForm):
    # просто форма для написания текста в 1 строку
    name = forms.CharField(label='Имя',
                           # обязательное для заполнения поле или нет
                           required=True,
                           # вид поля Textarea или TextInput
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Input animal name',
                                      'class': 'form-control', }
                           )
                           )

    category = forms.ModelChoiceField(
        label='Категория',
        # queryset - выборка
        queryset=Category.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    food = forms.ModelMultipleChoiceField(
        label='Еда',
        queryset=Food.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Animal
        fields = '__all__'
        # fields = ('name', 'category')
        # exclude = ('category',)


class ContactForm(forms.Form):
    # Наследование от простых форм, т.к. ничего не сохраняем в модель
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))