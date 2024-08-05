from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .models import MyUser
from .forms import RegistrationForm


class RegisterView(CreateView):
    template_name = 'user_app/register.html'
    model = MyUser
    form_class = RegistrationForm
    success_url = reverse_lazy('user_app:login')


class AuthView(LoginView):
    template_name = 'user_app/login.html'
