from django.shortcuts import render
from django.views import generic as views
# Create your views here.


class HomePageView(views.TemplateView):
    template_name = 'common/home.html'
