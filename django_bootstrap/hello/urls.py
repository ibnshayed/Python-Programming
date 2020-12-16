
from django.urls import path
from . import views

# app_name is used to define <a href="{% url 'hello:url_path_name' %}"> something </a>
app_name = 'hello'

urlpatterns = [
    path('', views.index, name='index'),
]
