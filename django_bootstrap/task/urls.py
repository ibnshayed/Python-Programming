from django.urls import path
from . import views

'''
when app_name include in the url file then
on html <a href="{% url 'task:path_name' %}"></a> --> will work
on html <a href="{% url 'path_name' %}"></a> --> will not work
'''
app_name = 'task'

urlpatterns = [
    path('', views.index, name='index'),
    path('addtask/', views.addtask, name='addtask'),
]

