from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/details/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/resolve/', views.task_resolve, name='task_resolve'),
]
