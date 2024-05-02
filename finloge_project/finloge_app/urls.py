from django.contrib import admin
from django.urls import path
from .views import index_page

urlpatterns = [
    path('coming_soon/', index_page,name='index'),
]