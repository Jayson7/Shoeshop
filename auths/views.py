from django.shortcuts import render

from django.views import generic
from django.views.generic import CreateView

from .forms import customerforms
from django.urls import reverse_lazy
# Create your views here.

from django.contrib.auth.forms import UserCreationForm

class Register(generic.CreateView):
      form_class = customerforms
      template_name = 'registration/register.html'
      
      success_url = reverse_lazy('login')
