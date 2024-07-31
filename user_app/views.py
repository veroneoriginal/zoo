from django.views.generic import TemplateView, CreateView
from .models import MyUser
from .forms import RegistrationForm


class RegisterView(CreateView):
    template_name = 'user_app/register.html'
    model = MyUser
    form_class = RegistrationForm
