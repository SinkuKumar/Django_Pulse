from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('table/', views.task_table, name='task_table'),
    path('kanban/', views.task_kanban, name='task_kanban'),
    path('gantt/', views.task_gantt, name='task_gantt'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/details/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/resolve/', views.task_resolve, name='task_resolve'),
    # path("table/", views.task_table, name="table"),
    # path("kanban/", views.task_kanban, name="kanban"),
    # path("calendar/", views.task_calendar, name="calendar"),
]
