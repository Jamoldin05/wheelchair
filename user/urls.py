from django.contrib import admin
from django.urls import path
from .views import login_page


app_name = 'user'


urlpatterns = [
    path('login/', login_page, name = 'login_page')
]