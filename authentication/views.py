from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    login_url = 'login'

class ContactPageView(LoginRequiredMixin ,TemplateView):
    template_name = 'contact.html'
    login_url = 'login'
    
class FeaturesPageView(LoginRequiredMixin ,TemplateView):
    template_name = 'features.html'
    login_url = 'login'