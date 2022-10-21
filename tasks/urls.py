from django.urls import path

from tasks.views import helloworld, taskList, yourName



urlpatterns = [
    path("helloworld/", helloworld),
    path('', taskList, name='task-list'),
    path('yourname/<str:name>', yourName, name='your-name')
]
