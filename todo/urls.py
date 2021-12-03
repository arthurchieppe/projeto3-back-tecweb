from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/todo/', views.api_all_tasks),
    path('api/todo/delete/<int:task_id>', views.api_delete_task),
]