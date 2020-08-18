from django.urls import path
from . import views

urlpatterns = [
    path('', views.overView, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
]
