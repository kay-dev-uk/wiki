from urllib.parse import urlparse
from django.urls import path

from . import views

urlpatterns = [
    path("str:title", views.title, name="title")
]



