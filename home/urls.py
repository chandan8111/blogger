from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('about', views.about, name='About Page'),
    path('contact', views.contact, name='Contact Us'),
    path('search', views.search, name='Search'),
    path('signup', views.handleSignup, name='Handle SignUp'),
    path('login', views.handleLogin, name='Handle Login'),
    path('logout', views.handleLogout, name='Handle Logout'),
]