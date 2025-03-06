from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.homepage,name="home"),
    path('tasks/', views.alltask, name="all_tasks"),
   
]