from django.urls import path
from . import views

urlpatterns = [
    # hozircha bo‘sh
]

from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
