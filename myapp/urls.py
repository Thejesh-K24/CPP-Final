from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('signup/', views.signup, name ='signup'),
    path('login/', views.login, name ='login'),
    path('traffic_update/', views.traffic_update, name ='traffic_update'),
    path('logout/', views.logout, name='logout'),  # Logout page
     
      ]
    
