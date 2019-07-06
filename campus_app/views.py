from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class HomeView(TemplateView):
    template_name="campus_app/home.html"

class ContatoView(TemplateView):
    template_name ="campus_app/contato.html"
