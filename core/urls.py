from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:game_id>/', views.display, name='display'),
]
