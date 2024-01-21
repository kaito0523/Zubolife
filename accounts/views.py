from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm  # 追加

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm  # 修正
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

