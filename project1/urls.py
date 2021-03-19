from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name = 'Home'),
path('login/', views.login, name = 'Login'),
path('investigate/', views.investigate, name = 'Investigate'),
path('addcase/', views.addcase, name = 'Addcase'),
]