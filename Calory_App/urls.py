from django.urls import path
from .views import *
urlpatterns = [
    path('',loginPage,name='login'),
    path('logout',logoutPage,name='logout'),
    path('register/',registerPage,name='register'),
    path('dashboard/',dashboardPage,name='dashboard'),
    path('profile/',profilePage,name='profile'),
    path('consumecalory/',consumeCaloryPage,name='consumecalory'),
]