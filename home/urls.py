from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('about/', views.about, name='About Page'),
    path('contact/', views.contact, name='Contact Us'),
]