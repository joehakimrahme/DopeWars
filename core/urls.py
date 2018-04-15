from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?P<game_id>[a-f0-9-]+)', views.display, name='display'),
]
