"""
excursions_markovav_ru URL Configuration
"""
from django.urls import path

from excursions_markovav_ru_main.views import views, login_views

urlpatterns = [
    path('add_excursions/', views.add_excursions_page, name='add_excursions'),
    path('excursions/', views.excursions_page, name='excursions'),
    path('login/', login_views.login_page, name='login'),
    path('logout/', login_views.logout_page, name='logout'),
    path('', views.index_page, name='index'),
]
