from django.urls import path
from . import views
from .views import (TaskListView,
                    TaskDetailView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView)


urlpatterns = [
    path('', TaskListView.as_view(), name="tasks-home"),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name="tasks-detail"),
    path('tasks/new/', TaskCreateView.as_view(), name="tasks-create"),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name="tasks-update"),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name="tasks-delete"),
    path('about/', views.about, name="tasks-about"),
]