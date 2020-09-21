from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="tasks-home"),
    path('about/', views.about, name="tasks-about"),
]