from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
]