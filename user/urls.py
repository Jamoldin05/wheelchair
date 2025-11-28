from django.contrib import admin
from django.urls import path
from .views import login_page,logout_page,register_page


app_name = 'user'


urlpatterns = [
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),
    path('register/',register_page,name='register_page'),
]