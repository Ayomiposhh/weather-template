from django.urls import path, include 
from weather__app import views
from django.contrib.auth import views as auth_views

# from weather__project import weather__app


app_name = 'weather__app'


urlpatterns = [

    path('home/', views.home, name='home'),
]