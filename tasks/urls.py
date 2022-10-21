from django.urls import path

from tasks.views import helloworld, taskList, yourName, taskView, newTask



urlpatterns = [
    path("helloworld/", helloworld),
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name="task-view"),
    path('newtask/', newTask, name="new-Task"),
    path('yourname/<str:name>', yourName, name='your-name')
]
