from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blogHome, name='BlogHome'),
    path('<str:slug>', views.blogPost, name='BlogPost'),
]