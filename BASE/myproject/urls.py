from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
]